"""
测试zendesk接口
"""

import requests

api_token = "chris@jadewireless.com/token:oUYQVyRaIGJ0PXFMMWd6r5FODGLRwkEyHbjtkfeb"

api_token_base64 = "Y2hyaXNAamFkZXdpcmVsZXNzLmNvbS90b2tlbjpvVVlRVnlSYUlHSjBQWEZNTVdkNnI1Rk9ER0xSd2tFeUhianRrZmVi"

sub_domain = "https://jadewirelesshelp.zendesk.com"

create_ticket_url = sub_domain + "/api/v2/tickets.json"

header = {
    "Authorization": "Basic " + api_token_base64,
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def create_ticket():
    response = requests.post(url=create_ticket_url,
                             headers=header,
                             data="""
                             {"ticket": {"subject": "My printer is on fire!","comment": {"body": "The smoke is very colorful."}}}
                             """)
    print(response.text)


if __name__ == '__main__':
    create_ticket()
