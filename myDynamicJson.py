import json

def empJson(fn, ln, age, sal, h1, h2, h3, fatherName, motherName, wn, count, n1, n2):
    emp = {
        "firstName": fn,
        "lastName": ln,
        "age": age,
        "salary": sal,
        "hobbies":[h1, h2, h3],
        "parents":{
            "fatherName": fatherName,
            "motherName": motherName
        },
        "wifeName":wn,
        "children":{
            "howMany": count,
            "names":[n1, n2]
        }
    }
    #return json.dumps(emp, indent=2)
    return json.dumps(emp)

if __name__ == '__main__':
    emp1 = empJson("Mark", "Tyson", 56, 123456789, "cricket","tennis", "dancing",
                   "Will", "Mary", "Lizy", 2, "Ann", "Jim")
    print(emp1)