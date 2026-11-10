"""pricefox: discount and price formatting helpers."""

from __future__ import annotations

import argparse


def apply_discount(price: float, discount_pct: float) -> float:
    """Apply a percentage discount to a price."""
    return price * (1 - discount_pct)


def format_price(amount: float) -> str:
    """Format an amount as a US dollar string."""
    return f"${amount:.2f}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pricefox")
    parser.add_argument("--price", type=float, required=True)
    parser.add_argument("--discount", type=float, required=True)
    args = parser.parse_args(argv)
    total = apply_discount(args.price, args.discount)
    print(f"{format_price(args.price)} at {args.discount}% off -> {format_price(total)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# gh resolution test
