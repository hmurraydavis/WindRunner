#1) Can you give an order of magnitude for the "quite large" voltage variation out of the Minisense 100 on p.4?
Comparing this statement to the measured data Figures 5-10, it seems you've divided down the minisense 100 output voltage so it is comparable to that of the ADXL, but it would be informative to know how much attenuation that required. 

#2) Please also include power consumption in Watts for the ADXL and BMP 180 (even if order-of-magnitude only), not just voltage range. If consumption is high, this could significantly factor into a design decision.

#3) Some minor formatting issues -- missing citation on p.3, and table formatting issues on pp 7-8. "Down hull" on p. 5 should be "downhaul."

4) The measured data in Figs. 5-10 should be displayed more clearly to highlight how interesting it is! It is very difficult to compare the "sail holds its shape" and "sail luffs" plots because the axes are different and in a tiny font. Making the axis labels larger and the ranges the same would help clarify these plots. 
Additionally, it would be nice to show the time-average data visually, for example in a third set of figures plotting the time window average data (or the variance data) for the "sail holds its shape" and "sail luffs" on the same axes so the difference can be seen. Although the data is given in the table, it may have more impact if it can be summarized graphically.


------------------------------------------------------------------------------


- I agree that the problem is interesting, but I am not so sure about the motivation. To me, 
it seems the assumptions and failures you mention on page 2 could better be checked with 
cheap, additional sensors. However, I agree that optimizing the sail trim for best performance 
is an intricate optimization problem. Conventionally, a human sailor would study the telltales 
in the sail's luff to optimize sail trim and course depending on the sailing conditions. 

- I am not sure I undestand how the sensors where mounted and how, for example, you could 
compensate the output offset (page 7). Please give more detail. 

#- Could you add a figure (picture) of your setup, including the sail? From your description, I don't fully understand the type of sail you've built.

- The point X position in Figures 5 - 10 seems to be the x coordinate of the camera image?! If 
so, please give more detail on camera calibration and a the image processing. Note that the 
centroid does not need to be at a pixel.  

- Revise Tables 3 and 4. 
#Typically, a table caption is above the table and 
should explain all detail in the table ('my caption' doesn't seem to do ...). 
#Also, I do not think the number of decimal places you give represents the precision of the sensors. Give 2 decimal places, and 
#give mean and standard deviation per trial, please.

- Figures 5 - 10 are MUCH too small. I need to be able to read the axis labels on paper, too!

#- Use a (shorter) running title (e.g., [] in Latex)
  
- Your references are full of typos!!

- You may want to check for previous work on sail shape detection -- I know of work at 
universities of Delft or Utrecht, where a pattern was projected into the sail and at Heinrich 
Hertz Institute, where fiber Bragg gratings were embedded into the sails.

------------------------------------------------------------------------------


The topic of the paper fits the scope of the IRSC, as it addresses an analysis of different sensors for detecting sail luffing. Such detection is paramount to improve the performance of a robotic sailboat, however the title of the paper is misleading, as it suggests a comparison of different methods of detection. Instead, the authors compare the performance of three different sensors, each with its own technology. It is not clear how can they be representative of the technology, since none of the criteria for selection was performance. 

This work should only be published if subject to a major review. Overall, the quality of presentation is poor, with many qualitative remarks and interpretations that should not be present in a scientific paper. 
#For example, for the purpose of the paper, all second paragraph of section 2 is pointless. 
The same for the references to the shops and websites where it is cheaper to buy the sensors (section 3.1). 
This information is prone to become obsolete at the time of publication and provides no scientific value. 
Also, too much detail on the format of the strings and files on the experimental setup. It would be sufficient to say the data was saved on file for later processing.

In the description of the experimental setup, a picture or a diagram with dimensions could be used to document it. It should also be shown how the camera was used to provide groundtruth. What was the delay on camera image analysis?

In section 3.4, data analysis is quite poor and there is an abuse of current language instead of scientific language: "sensor output ... is more erratic"; "it also varies more and at a greater frequency"; "the sail luffs more or less evenly"... None of this is quantified as it should be.

Tables 3 and 4 have no captions and badly formatted. It is not clear how can the authors take any conclusions from these data. More, there is no indication of the accuracy of the table entries, but the number of significant digits seems to be greatly exagerated. All in all, there is no indication how the sensor data could be used on an autonomous system to declare that a sail is luffing. If a certain threshold were used, how many false positives/negatives would be detected?

In section 4, the author are only concerned with minor practical aspects, like diodes in series and i2c interfaces. There is no quantitative comparison of performance. Again, expressions such as "it outputs significant signal noise" should be replaced by quantitative measures, like SNR or figures like mean and standard deviation.

There is an abuse of website references, badly formatted.

