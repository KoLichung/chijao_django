import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError

def run():
  try:
    mailchimp = MailchimpTransactional.Client('SQtcqkSt9MApMYOlAcvrQQ')
    response = mailchimp.users.ping()
    print('API called successfully: {}'.format(response))
  except ApiClientError as error:
    print('An exception occurred: {}'.format(error.text))



def test_mail_to_jason():
    print('send mail to jason@kosbrother.com')

    mailchimp = MailchimpTransactional.Client('SQtcqkSt9MApMYOlAcvrQQ')
    message = {
        "from_email": "manny@mailchimp.com",
        "subject": "Hello world",
        "text": "Welcome to Mailchimp Transactional!",
        "to": [
        {
            "email": "jason@kosbrother.com",
            "type": "to"
        }
        ]
    }

    try:
      response = mailchimp.messages.send({"message":message})
      print('API called successfully: {}'.format(response))
    except ApiClientError as error:
      print('An exception occurred: {}'.format(error.text))


