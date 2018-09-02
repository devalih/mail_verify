import csv

import dns.resolver

def main():
    with open("mails.csv", "rt") as csvin:
        with open('mails_clean.csv', 'w') as csvout:
            csv_read = csv.reader(csvin)
            csv_write = csv.writer(csvout)
            domains = {}
            for row in csv_read:
                if row:
                    domain = row[0].split("@")[-1]
                    if domain in domains:
                        if domains[domain]:
                            csv_write.writerow(row)
                    else:
                        print(domain)
                        try:
                            dns.resolver.query(domain, 'MX')
                            print("Yes")
                            domains[domain] = True
                            csv_write.writerow(row)
                        except dns.exception.DNSException as e:
                            print("No", e)
                            domains[domain] = False

            print(domains)
if __name__ == "__main__":
    main()

