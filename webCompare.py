import urllib3

url = 'https://www.amazon.jobs/en/jobs/475965/technical-program-manager-ii-amz1667'

http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
resp = http.request('GET', url)


# Read in the HTML response
html_bytes = resp.data
html = html_bytes.decode("utf-8")

# Get the text body
title_index = html.find("<main>") # location of title start
start_index = title_index + len("<main>")  # actual title text
end_index = html.find("</main>") # location of closing bracket
main_txt = html[start_index:end_index]


print(main_txt)