country_code={"india":"0091",
              "australia":"0025",
              "nepal":"00977"}
print("the country code for india")
print(country_code.get("india","not found"))
print("the country code for usa")
print(country_code.get("usa","not found"))