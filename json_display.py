import json
import pandas as pd




def display_json():
    # pwned = pd.read_json('/pwned.json', orient='index')
    # print pwned
    print "hello"
    with open("/pwned.json") as pwned:
        d = json.load(pwned)
        pwncount = d.get('PwnCount', '')
        site = d.get('Title', '')
        date = d.get('BreachDate', '')
        description = d.get('Description', '')
        classes = d.get ('DataClasses', '')
    df = pd.DataFrame([pwncount, site, date, description, classes]).T


    # pwned_df = pd.DataFrame()
    # count = 0;
    # for l in open("/pwned.json"):
    #     try:
    #         count += 1
    #         if (count == 20001):
    #             break
    #         obj1 = json.loads(l)
    #         df1 = pd.DataFrame(obj1, index=[0])
    #         pwned_df = pwned_df.append(df1, ignore_index=True)
    #     except ValueError:
    #         line = line.replace('\\', '')
    #         obj = json.loads(line)
    #         df1 = pd.DataFrame(obj, index=[0])
    #         pwned_df = pwned_df.append(df1, ignore_index=True)



def main():
    display_json()

main()
