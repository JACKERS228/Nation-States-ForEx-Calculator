# The NationStates Currency Exchanger
This is a currency converter for the online game NationStates (NS). It is intended to run natively on your machine and leverages the NationStates API to dynamically update currency statistics daily.
## Setting Up
Luckily, setting up is very easy!
* When you first open the app, it will ask you if you'd like to update the "daily dump" files from NationStates. If you want accurate numbers, it is reccomended that you update them. This should take about 10-15 seconds as they are large files.
>Note: If it is the first time you are opening the app, you **must** do this, as the necessary files are not present yet or, if you prefer, you can download the required .gz files at [this link](https://www.nationstates.net/pages/api.html#dumps).
> 1) Click the two links, the first under "Regions" and the second under "Nations."
> 2) Download them to your PC and move them to where this app is installed. Look for a folder called `.../dumps` and place them there.
> 3) Extract the XML files to the dumps folder, make sure the XML files themselves are in the `dumps` folder and not inside their folders they are extracted into.
> 4) Delete the extra folders and open the app.
* The app will then ask you for the first nation you would like to compare. Enter the name **exactly** as it appears on NS. So in the case of "Rhaza", enter it exactly as "Rhaza" and *not* "rhaza". This is because the app is looking for your unique nation in the XML file as it was entered.
* Next, the app will produce the name of the nation, its currency, and the average annual income according to the NationStates API. Then, it will ask you for the second nation and the process will repeat.
* Finally, it will calculate the exchange rate as `"1 of Nation 1's currency is about 2.7 Nation 2's Currency"` and give you some statistics about your country's economic situation based on the buying power of the currency.
* You can choose to do another conversion or quit, which closes the app.
