import argparse

from dotenv import load_dotenv

from amazon_pricer.amazon_pricer import AmazonPricer

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Amazon Price Scraper",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("--url", type=str, help="Amazon URL of the desired object")

    parser.add_argument(
        "--user_agent",
        type=str,
        help="user-agent of your browser",
    )

    parser.add_argument(
        "--current_price",
        type=float,
        help="current price of the object",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()
    headers = {"User-Agent": args.user_agent}
    amazon_pricer = AmazonPricer(
        url=args.url, headers=headers, current_price=args.current_price
    )
    amazon_pricer.check_price()
