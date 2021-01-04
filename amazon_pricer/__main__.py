import argparse
import os

from dotenv import load_dotenv

from amazon_pricer.amazon_pricer import AmazonPricer
from amazon_pricer.yaml_reader import YamlReader

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Amazon Price Scraper",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--user_agent",
        type=str,
        default="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
        help="user-agent of your browser",
    )

    parser.add_argument(
        "--filepath_yaml",
        type=str,
        default=os.path.join(
            os.path.dirname(__file__),
            "../database.yaml",
        ),
        help="filepath to the YAML config file",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()
    headers = {"User-Agent": args.user_agent}
    all_items = YamlReader(pathfile=args.filepath_yaml).get_elements()
    for item in all_items:
        print(f"Checking for price changes for {item['name']}")
        amazon_pricer = AmazonPricer(
            url=item["url"], headers=headers, current_price=item["current_price"]
        )
        amazon_pricer.check_price()
        print(f"Check has been done, if the price has decreased you will receive an email!")
