from twilio.rest import Client
from datetime import timedelta, datetime
import time
import yfinance as yf

account_sid = "ACa9b1a8f47563e651a27df1a07ee3693d"
auth_token = "676c2333a547a82de3d70dac610c3687"
client = Client(account_sid, auth_token)
def send_sms(to, message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{to}'
        )
        print("Message sent Successfully : ", message.sid)
    except Exception as e:
        print(e)


def financial_data_of_company(ticker):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    info = stock.info
    return info


def message_creator(info, max_length=1599):
    if not info:
        return "No stock data available."
    required_keys = ['longName', 'sector', 'industry', 'marketCap', 'trailingPE']
    if all(key in info for key in required_keys):
        m = (
            f"Company: {info['longName']}\n"
            f"Sector: {info['sector']}\n"
            f"Industry: {info['industry']}\n"
            f"Market Cap: {info['marketCap']}\n"
            f"P/E Ratio: {info['trailingPE']}"
        )
        return m
    else:
        lines = []
        current_length = 0

        for key, value in info.items():
            formatted_key = ''.join([' ' + char if char.isupper() else char for char in key]).strip().title()
            line = f"{formatted_key}: {value}"

            # Check if adding this line exceeds max length
            if current_length + len(line) + 1 > max_length:  # +1 for newline or space
                break

            lines.append(line)
            current_length += len(line) + 1

        return "\n".join(lines)


def controller(phone_number, company_name):
    receiver = phone_number
    info = financial_data_of_company(company_name)
    message = message_creator(info)
    send_sms(receiver, message)
    print("Message sent")

