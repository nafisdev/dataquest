## 3. Using Bayes' Theorem ##

p_spam = 0.5
p_non_spam = 0.5
p_new_message = 0.5417
p_new_message_given_spam = 0.75
p_new_message_given_non_spam = 0.3334

p_spam_given_new_message=(p_spam*p_new_message_given_spam)/p_new_message

p_non_spam_given_new_message=(p_non_spam*p_new_message_given_non_spam)/p_new_message

classification='spam' if p_spam_given_new_message>p_non_spam_given_new_message else 'non-spam'

## 4. Ignoring the Division ##

p_spam = 0.5
p_non_spam = 0.5
p_new_message_given_spam = 0.75
p_new_message_given_non_spam = 0.3334

p_spam_given_new_message=(p_spam*p_new_message_given_spam)

p_non_spam_given_new_message=(p_non_spam*p_new_message_given_non_spam)

classification='spam' if p_spam_given_new_message>p_non_spam_given_new_message else 'non-spam'

## 5. A One-Word Message ##

p_spam_given_secret = 8/21

p_non_spam=1/3
p_spam_and_secret=2/3*p_spam_given_secret
p_secret_given_non_spam=1/4

p_non_spam_given_secret=p_non_spam*p_secret_given_non_spam

classification='spam' if p_spam_given_secret > p_non_spam_given_secret else 'non-spam'

## 6. Multiple Words ##

p_spam_given_w1_w2_w3_w4 = 64/4802

p_non_spam_given_w1_w2_w3_w4=1/2*2/9*1/9*2/9*2/9
classification= 'spam' if p_non_spam_given_w1_w2_w3_w4<p_spam_given_w1_w2_w3_w4 else 'non-spam'

## 9. Edge Cases ##

p_spam = 2/4
p_secret_given_spam = 4/7
p_the_given_spam = 0/7
p_money_given_spam = 2/7
p_spam_given_message = (p_spam * p_secret_given_spam *p_the_given_spam*
                         p_money_given_spam)

p_non_spam_given_message=1/2*2/9*1/9*0

print(p_spam_given_message)



## 10. Additive Smoothing ##

p_spam = 2/4
p_secret_given_spam = (4 + 1) / (7 + 9)
p_the_given_spam = (0 + 1) / (7 + 9)
p_money_given_spam = (2 + 1) / (7 + 9)
p_spam_given_message = (p_spam * p_secret_given_spam *
                        p_the_given_spam * p_money_given_spam)
                        
p_non_spam_given_message=1/2 *(3/18)*(2/18)*(1/18)


classification='spam' if p_spam_given_message > p_non_spam_given_message else 'non-spam'     
                        