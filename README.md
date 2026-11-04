# portfolio-optimization-eurostoxx

Portfolio construction on 25 Euro Stoxx 50 stocks (monthly data, 10 years), from the opportunity set to constrained
optimization and an interactive backtest. 

## What is in the notebook

1. **Opportunity set** – log returns, annualized statistics, Jarque-Bera normality tests, correlation heatmap and hierarchical clustering.
2. **Estimation** – historical mean/covariance versus the **Single Index Model** (OLS betas on the Euro Stoxx 50), with **Vasicek** shrinkage of the betas.
3. **Optimization** (`scipy.optimize`, SLSQP) with institutional constraints: long-only, 10% single-name cap, 15% sector caps (energy, autos).
   - Tangency (max Sharpe) and global minimum variance portfolios
   - HHI-based concentration control
   - **Kataoka safety-first** criterion (maximize `mu - z*sigma` at 95% confidence)
   - **Elton-Gruber-Padberg cutoff rate (C\*)** versus Vasicek-adjusted inputs, with and without constraints
4. **Interactive backtest** – a Tkinter app to change weights, period and capital and compare against the benchmark.

## Run it

```bash
pip install -r requirements.txt
python make_sample_data.py          # synthetic data, see data/README.md
jupyter notebook notebooks/asset_management_takehome.ipynb
```

The stored cell outputs come from the original dataset. With the synthetic sample every cell runs, but the numbers
will differ and have no economic meaning. The Tkinter cell needs a desktop session.

## Notes and limitations

- Expected returns estimated from 120 monthly observations are noisy; that is why the notebook compares historical inputs with SIM and Vasicek-adjusted inputs.
- The risk-free rate is the last observed Bund 10Y yield, a constant approximation of the short rate.
- In-sample optimization: no out-of-sample test of the final weights beyond the interactive backtest.

## License

MIT (code). Data not included. Author: Vittorio Iacovoni ([vittorioiacovoni.com](https://vittorioiacovoni.com)).
