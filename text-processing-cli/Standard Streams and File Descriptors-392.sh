## 1. Standard Streams ##

/home/dq$ find / -name 'dq' 2> stderr

## 3. Redirecting Two Streams ##

/home/dq$ cat all_output

## 6. Duplicating File Descriptors ##

/home/dq$ ls /dev/null /home/inexistent 1>/dev/null 2>&1

## 7. Order of Redirections ##

/home/dq$ diff -y redirection_order order_verification

## 8. Standard Input ##

u/home/dq$ cat sorted_stdin

## 9. Redirecting Standard Input ##

/home/dq$ tr aeiou AEIOU 0<sorted_stdin 1>mad_vowels