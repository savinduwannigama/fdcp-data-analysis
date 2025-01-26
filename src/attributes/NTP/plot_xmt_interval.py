import matplotlib.pyplot as plt
import os


import json

# Specify the path to your JSON file
json_file_path = "xmt_arrays.json"

# Open the JSON file
with open(json_file_path, "r") as json_file:
    # Parse the JSON content
    device_xmt_intervals = json.load(json_file)


# device_g01 = ['AwairAirQuality', 'TPLinkCamera', 'AmazonEcho', 'SamsungCamera']

# binss0 = range(0, 150000, 1000)
binss1 = range(0, 90000, 1000)
# binss2 = range(0, 20000, 500)
# binss3 = range(0, 1000, 100)
# binss4 = range(0, 100, 1)
# binss4 = range(0, 1, .01)

for device, css in device_xmt_intervals.items():
    # if device not in device_g01:
    #     continue
    device_name = device
    print(f"device: {device}, len(css): {len(css)}")
    # if '/' in device:
    #     device_name = device.split('/')[0]

    # if device_name in printed_devices:
    #     continue
    # print(f'device_name: {device_name}')

    clean_data = css
    # clean_data = remove_outliers(css, 0)

    # Create a histogram with probabilities
    n, bins, _ = plt.hist(clean_data, bins=binss1, density=True, alpha=0.7)

    # Calculate bin widths
    bin_widths = bins[1] - bins[0]

    # Calculate relative frequencies (probabilities) for each bin
    probabilities = n * bin_widths

    # Plot the histogram with probabilities
    # plt.clf()  # Clear previous plot
    if device == "AwairAirQuality":
        labell = "Awair air quality"
    elif device == "TPLinkCamera":
        labell = "TPLink camera"
    elif device == "AmazonEcho":
        labell = "Amazon Echo"
    elif device == "SamsungCamera":
        labell = "Samsung camera"
    plt.bar(
        bins[:-1],
        probabilities,
        width=bin_widths,
        align="edge",
        alpha=0.7,
        label=labell,
    )

    # break


plt.xticks(range(0, 90001, 5000), rotation="vertical")
plt.xlim(0, 90000)

plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

plt.xlabel("Transmit Timestamp (xmt) Intervals (s)")
plt.ylabel("Probability: P[xmt = x]")
# plt.title('Line Plot from List')
plt.grid(True)
plt.legend()

final_output_dir = ""  # directory to save fig
plt.savefig(
    os.path.join(final_output_dir, "delta_transmit_timestamp.pdf"), format="pdf"
)  # save
plt.show()
