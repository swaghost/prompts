# Website Payment Setup Walkthrough

## Prompt

```
I want to charge [PRICE] for this: [DESCRIBE PRODUCT OR SERVICE]. Add the simplest payment option that works with the page you just built. Walk me through the setup one step at a time and tell me exactly what to copy from where. Do not ask me to paste private keys into chat. Use sandbox or test mode first, explain any required account, checkout, webhook, or backend step, then test and show me how to verify a payment going through safely.
```

## Output Requirements

- Recommend the simplest suitable payment provider based on country, currency, product type, and platform.
- Use hosted checkout or secure provider integrations where possible.
- Never place secret keys in HTML, JavaScript, screenshots, or public repositories.
- Walk through setup one step at a time and stop after each step until the user says `done`.
- Use test mode before live mode and explain how to verify success, failure, cancellation, refund, and fulfillment states.
