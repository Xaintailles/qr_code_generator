# qr_code_generator
Just a quick way to generate custom QR codes

For security reason, we are ignoring the json file necessary to create the QR code. Here is an example of the format expected.

```
{
    "example_key": {
        "link": "https://example.com",
        "logo_path": "./assets/foo.jpg",
        "account_name": "@bar"
    }
}
```