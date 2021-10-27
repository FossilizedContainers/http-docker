import requests

def main():
   # creating a dictionary to send the LiPD file to the server
   files = {"pond": open("static/3MPond.Pellatt.2000.lpd", 'rb')}
   # creating a variable that will recieve the netCDF file from the response message and sending the file(s) to the client
   netCDF = requests.post('http://127.0.0.1:4000/', files=files)
   # printing the file that the client recieved back from the srever in the response message
   print(netCDF.content)

if __name__ == "__main__":
   main()
