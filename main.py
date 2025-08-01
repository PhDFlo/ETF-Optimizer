from DCA.ETF import ETF
from DCA.Portfolio import PortfolioETF
import numpy as np


def main():

    # Create an ETF instance
    etf1 = ETF(
        name="Amundi MSCI World UCITS ETF",
        ticker="AMDW",
        currency="Euro",
        price=500.0,
        fees=0.2,
    )
    etf2 = ETF(
        name="Vanguard S&P 500 UCITS ETF",
        ticker="VUSA",
        currency="USD",
        price=300.0,
        fees=0.1,
    )
    etf3 = ETF(
        name="iShares Core MSCI Emerging Markets IMI UCITS ETF",
        ticker="EIMI",
        currency="Euro",
        price=200.0,
        fees=0.25,
    )

    # Create a PortfolioETF instance
    portfolio = PortfolioETF()
    portfolio.add_etf(etf1, target_share=0.5, amount_invested=2000.0)
    portfolio.add_etf(etf2, target_share=0.2, amount_invested=800.0)
    portfolio.add_etf(etf3, target_share=0.3, amount_invested=300.0)

    # Compute the actual share
    portfolio.compute_actual_shares()

    # Solve for equilibrium
    portfolio.solve_equilibrium(Investment_amount=1000.0, Min_percent_to_invest=0.99)

    # Print portfolio info and its keys/values
    info = portfolio.get_portfolio_info()
    print("\nPortfolio info:")
    for etf_info in info:
        print("ETF:")
        for k, v in etf_info.items():
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
