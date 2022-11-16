# priced in whatever #



<img width="950" alt="Screen Shot 2022-10-03 at 17 07 32" src="https://user-images.githubusercontent.com/95490556/193598178-60366faa-56bd-4266-b415-fd5b7915662a.png">




## about priced in whatever ##
priced in whatever (piw) is a python web app built for one function, measuring assets against other assets. piw allows users to price any asset in another. an example of this would be pricing spy (sp 500 ETF) in aapl (apple stock) to see how many apple shares 1 spy share can buy over time. the utility in this is that most assets are priced against a currency like the u.s. dollar or the euro. although this is a standard measuring stick, it does not give an investor a clear picture of the return of a stock relative to other assets. 

## why we built piw ##
beyond piw being a fun project for us to conceive and develop, there is real utility in seeing an asset priced in another asset. we wanted to build a tool for investors to gauge the returns of assets against other assets, given the theory that traditional measuring sticks of value in markets do not always represent actual returns over long-term horizons. in the example given above, pricing spy in apple stock provides the user with a visualization of how spy has faired relatively to apple stock by the number of apple shares it can buy over time. in this case, if you use piw, you will notice that spy has faired poorly against apple, meaning that over time spy has bought less and less apple stock. moreover, this gives someone an idea of how an asset's "alpha," fancy for relative performance, measures up against another asset. 

traditional equity markets will price equities against the currency of that market. given that apple is traded on the new york stock exchange, it is measured in u.s. dollars. the issue that arises from this is that the u.s. dollar, alongside most fiat currencies, has been a poor measuring stick of value. alternatively, if one were to use piw, one could gauge the performance of an asset against another measuring stick of value. take, for example, gold; if, for theoretical purposes, apple's return to date was 20%, an investor would most likely credit himself for having made a good investment given that the broad market returns typically 6% year over year. however! if gold in that same period returned 20% as well, then pricing apple in gold would result in a real return of 0%! that, after all, is a much poorer return than the original 20%. now, what does this exactly tell us? first off, it tells us that apple's return of 20% was against u.s. dollars, meaning that from the beginning of the period to the end, apple stock bought 20% more u.s. dollars than it did initially. in the case of gold, however, apple stock bought as much gold at the beginning as it did in the end, meaning there was no real return. this is as much of a testament to the return of apple as it is to the purchasing power of the measuring stick of value, in this case, gold. 

## how to use piw ##
piw is a bare-bone web app. we aimed to make something light and simple to use in the ethos that less is more. 

on the home page, there are two input boxes. the first box is used to type in the asset ticker you would like to have priced in the base asset. spy priced in aapl, goog priced in amd, tsla priced in gc=f (gold ounces), etc...

up till now, all inputs have been assets that use the same base currency, u.s. dollars. but what if you want to price a canadian stock in an american stock? fortunately, this has been built into the piw algorithm so that both assets are given the same base currency to provide an accurate picture of what x is worth in y. for example if you were to price enb.to (enbridge) in aapl, what would happen is that aapl would be converted into canadian dollars at the current exchange rate and then enb.to be priced in the canadian dollar version of aapl stock. 

since piw is built using the yahoo finance library for financial data, any ticker available on yf can be used on piw. it is essential to use the ticker and not the stock name and to make sure that you use all parts of the ticker for the app to work correctly. if a stock has a market suffix such as ".to" for stocks traded on the toronto stock exchange, it is necessary to include this in the ticker input.

## why use piw ##
piw is an open-source project; therefore, those who want can use it under the creative commons license. there are many reasons to use piw, as mentioned throughout this article; however, the most apparent is the ability to get a unique insight into market pricing. 

whether you are fascinated by markets and/or looking to better understand an asset's value and correlation to other assets, piw enables you to do so.

as should be mentioned, piw is not perfect; therefore, do not make investments based on data given by piw. piw is a tool intended for educational purposes solely. 

## who we are ##
Noam Rosner is an undergraduate student studying computer science in tel aviv, israel. Noam is passionate about building unique apps. moreover, Noam is an avid musician and creator with an eye for design.

Zachary Merhi is an undergraduate student at mcgill university studying economics. Zachary has a strong interest in financial markets and their functioning. 

## contact and collaboration ##
we appreciate feedback and recommendations as it helps us make piw a better tool for all. moreover, if you have an idea you would like to share related to piw, feel free to contact us.
