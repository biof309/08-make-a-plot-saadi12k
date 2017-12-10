#use matplotlib to plot data
import matplotlib.pyplot as plt
x = [974.58033839999996, 5937.0295259999984, 6223.3674650000003, 4797.2312670000001, 12779.379639999999, 34435.367439999995, 36126.492700000003, 29796.048340000001, 1391.253792, 33692.605080000001, 1441.2848730000001, 3822.137084, 7446.2988029999997, 12569.851769999999, 9065.8008250000003, 10680.792820000001, 1217.0329939999999, 430.07069159999998, 1713.7786860000001, 2042.0952400000001, 36319.235009999997, 706.01653699999997, 1704.0637240000001, 13171.638849999999, 4959.1148540000004, 7006.5804189999999, 986.14787920000003, 277.55185870000003, 3632.5577979999998, 9645.06142, 1544.7501119999999, 14619.222719999998, 8948.1029230000004, 22833.308509999999, 35278.418740000001, 2082.4815670000007, 6025.3747520000015, 6873.2623260000009, 5581.1809979999998, 5728.3535140000004, 12154.089749999999, 641.36952360000021, 690.80557590000001, 33207.0844, 30470.0167, 13206.48452, 752.74972649999995, 32170.37442, 1327.6089099999999, 27538.41188, 5186.0500030000003, 942.6542111, 579.23174299999982, 1201.637154, 3548.3308460000007, 39724.978669999997, 18008.944439999999, 36180.789190000003, 2452.210407, 3540.6515639999998, 11605.71449, 4471.0619059999999, 40675.996350000001, 25523.277099999999, 28569.719700000001, 7320.8802620000015, 31656.068060000001, 4519.4611709999999, 1463.249282, 1593.06548, 23348.139730000006, 47306.989780000004, 10461.05868, 1569.3314419999999, 414.5073415, 12057.49928, 1044.7701259999999, 759.34991009999999, 12451.6558, 1042.581557, 1803.151496, 10956.991120000001, 11977.57496, 3095.7722710000007, 9253.896111, 3820.1752299999998, 823.68562050000003, 944.0, 4811.0604290000001, 1091.359778, 36797.933319999996, 25185.009109999999, 2749.3209649999999, 619.67689239999982, 2013.9773049999999, 49357.190170000002, 22316.192869999999, 2605.94758, 9809.1856360000002, 4172.8384640000004, 7408.9055609999996, 3190.4810160000002, 15389.924680000002, 20509.64777, 19328.709009999999, 7670.122558, 10808.47561, 863.08846390000019, 1598.4350890000001, 21654.83194, 1712.4721360000001, 9786.5347139999994, 862.54075610000018, 47143.179640000002, 18678.314350000001, 25768.257590000001, 926.14106830000003, 9269.6578079999999, 28821.063699999999, 3970.0954069999998, 2602.3949950000001, 4513.4806429999999, 33859.748350000002, 37506.419070000004, 4184.5480889999999, 28718.276839999999, 1107.482182, 7458.3963269999977, 882.9699437999999, 18008.509239999999, 7092.9230250000001, 8458.2763840000007, 1056.3801209999999, 33203.261279999999, 42951.65309, 10611.46299, 11415.805689999999, 2441.5764039999999, 3025.3497980000002, 2280.769906, 1271.211593, 469.70929810000007]
y = [43.828000000000003, 76.423000000000002, 72.301000000000002, 42.731000000000002, 75.319999999999993, 81.234999999999999, 79.828999999999994, 75.635000000000005, 64.061999999999998, 79.441000000000003, 56.728000000000002, 65.554000000000002, 74.852000000000004, 50.728000000000002, 72.390000000000001, 73.004999999999995, 52.295000000000002, 49.579999999999998, 59.722999999999999, 50.43, 80.653000000000006, 44.741000000000007, 50.651000000000003, 78.552999999999997, 72.960999999999999, 72.888999999999996, 65.152000000000001, 46.462000000000003, 55.322000000000003, 78.781999999999996, 48.328000000000003, 75.748000000000005, 78.272999999999996, 76.486000000000004, 78.331999999999994, 54.790999999999997, 72.234999999999999, 74.994, 71.338000000000022, 71.878, 51.578999999999994, 58.039999999999999, 52.947000000000003, 79.313000000000002, 80.656999999999996, 56.734999999999999, 59.448, 79.406000000000006, 60.021999999999998, 79.483000000000004, 70.259, 56.006999999999998, 46.388000000000012, 60.915999999999997, 70.198000000000008, 82.207999999999998, 73.338000000000022, 81.757000000000005, 64.698000000000008, 70.650000000000006, 70.963999999999999, 59.545000000000002, 78.885000000000005, 80.745000000000005, 80.546000000000006, 72.566999999999993, 82.602999999999994, 72.534999999999997, 54.109999999999999, 67.296999999999997, 78.623000000000005, 77.588000000000022, 71.992999999999995, 42.591999999999999, 45.677999999999997, 73.951999999999998, 59.443000000000012, 48.302999999999997, 74.241, 54.466999999999999, 64.164000000000001, 72.801000000000002, 76.194999999999993, 66.802999999999997, 74.543000000000006, 71.164000000000001, 42.082000000000001, 62.069000000000003, 52.906000000000013, 63.784999999999997, 79.762, 80.203999999999994, 72.899000000000001, 56.866999999999997, 46.859000000000002, 80.195999999999998, 75.640000000000001, 65.483000000000004, 75.536999999999978, 71.751999999999995, 71.421000000000006, 71.688000000000002, 75.563000000000002, 78.097999999999999, 78.746000000000024, 76.441999999999993, 72.475999999999999, 46.241999999999997, 65.528000000000006, 72.777000000000001, 63.061999999999998, 74.001999999999995, 42.568000000000012, 79.971999999999994, 74.662999999999997, 77.926000000000002, 48.158999999999999, 49.338999999999999, 80.941000000000003, 72.396000000000001, 58.555999999999997, 39.613, 80.884, 81.701000000000022, 74.143000000000001, 78.400000000000006, 52.517000000000003, 70.616, 58.420000000000002, 69.819000000000003, 73.923000000000002, 71.777000000000001, 51.542000000000002, 79.424999999999997, 78.242000000000004, 76.384, 73.747, 74.248999999999995, 73.421999999999997, 62.698, 42.383999999999993, 43.487000000000002]
print(x[-1]);print(y[-1])
plt.plot(x,y)
plt.show()
#Scatter plot is a better representation of the data
plt.scatter(x,y)
plt.show()
