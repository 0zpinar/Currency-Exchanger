import os
import requests
import json
import datetime

def path():
    try:
        appData_path = os.environ.get("APPDATA")
        dirName = "CurrencyConverter"
        newDirPath = os.path.join(appData_path, dirName)
        os.makedirs(newDirPath, exist_ok=True)
    except FileExistsError:
        newDirPath = os.path.join(appData_path, dirName)
    return newDirPath

def useData():
    pathDir = path()
    filePath = os.path.join(pathDir, "data.txt")
    if os.path.exists(filePath):
        with open(filePath, 'r') as data:
            readData = data.read()
        return readData
    else:
        with open(filePath, "w") as data:
            readData = input("Country Currency:")
            data.write(readData)
        return readData


def useApi(api: str, readData: str):
    getDataUsa = requests.get(f"https://v6.exchangerate-api.com/v6/{api}/latest/USD")
    getDataUsa_json = json.loads(getDataUsa.text)
    print("1 {0} = {1} {2}".format("USD", getDataUsa_json["conversion_rates"][readData], readData))

    getDataEur = requests.get(f"https://v6.exchangerate-api.com/v6/{api}/latest/EUR")
    getDataEur_json = json.loads(getDataEur.text)
    print("1 {0} = {1} {2}".format("EUR", getDataEur_json["conversion_rates"][readData], readData))

    give = input("Exchange Currency:")
    give = give.upper()
    hMuch = int(input("Enter the Amount of Money to Exchange:"))
    get = input("Currency to Receive:")
    get = get.upper()

    getDataCh = requests.get("https://v6.exchangerate-api.com/v6/{0}/latest/{1}".format(api, give))
    getDataCh_json = json.loads(getDataCh.text)
    converted_amount = hMuch * getDataCh_json["conversion_rates"][get]
    print("{0} {1} = {2} {3}".format(hMuch, give, converted_amount, get))


def main():
    readData = useData()
    print(datetime.datetime.now())
    while True:
        try:
            useApi("abc123", readData) #Enter your own API key in the API section.
            exitFlag = input("Q for Exit")
            if exitFlag:
                break
        except KeyError:
            print("Currency Not Found")
            exitFlag = input("Q for Exit")
            if exitFlag:
                break
        except ValueError:
            print("Please Enter a Number")
            exitFlag = input("Q for Exit")
            if exitFlag:
                break

if __name__ == "__main__":
    main()
