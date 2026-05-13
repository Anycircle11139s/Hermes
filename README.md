This is my Hermes Project:
Ngl, I created my hermes project cause I was bored and thought it would be a good idea, also, when I started it was a tier 2 project and said it would only take 5 hours... Later it would change to tier 1 with 10 hours :(

I mostly enjoyed the project, it helped me learn about resistors and datasheets, also it wasn't to complex. I'm also glad we don't have to CAD a case, because that would just be annoying.

<img width="892" height="370" alt="Screenshot 2026-04-10 at 1 38 36 pm" src="https://github.com/user-attachments/assets/e5535099-cd93-43f9-8c69-77cc0acf36bf" />


The schematic took me a while because I had to find the footprint and symbol for my chosen sensor (temp and humidity sensor). I also had to learn about how to use my resistors from people in slack. It was an educational experience.

<img width="659" height="645" alt="Screenshot 2026-04-10 at 1 38 48 pm" src="https://github.com/user-attachments/assets/20de1267-d235-4302-bae5-287f7b5b36b4" />

The PCB was fairly easy for me, because I'm used to more complex projects such as hackpads and split keyboards (which require a lot more routing and pain), so the Hermes project was a nice break. Once I finished the PCB, I added the silkscreen layer. 


I spent the most time on the BOM because getting all the parts under $25 USD was difficult, but I eventually managed it. I originally started with 3 different companies (LCSC, JLCPCB and Ali-express), this wouldnt work because of the 3 seperate shipping cost, 2 hours later, I finally got it to under $25 USD even tho I still had 3 different companies, which included digikey, ali-express and JLCPCB, JLCPCB was 5.50 total, I got the oled and rotary encoder from ali express because of cheap prices and free shipping, I got the rest of the parts from digikey because they had the cheapest parts even though digikey had a 6.99 USD shipping fee along with two dollars in tariffs/tax.


|Name                     |Purpose                                              |Quantity|Total Cost (USD)|Link                                                                                                                                                                                     |Distributor|
|-------------------------|-----------------------------------------------------|--------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|Oled                     |screen                                               |1       |2.30            |https://www.aliexpress.com/item/1005006636072295.html?mp=1&pdp_npi=6@dis!USD!USD%203.47!USD%200.99!!USD%200.99!!!@2102f22c17753786454871604ea4a4!12000037978554141!ct!AU!7402515296!!1!0!|ali=express|
|resistor                 |for ressisting                                       |36      |0.98            |https://www.digikey.com/en/products/detail/stackpole-electronics-inc/CF12JT4K70/1741152                                                                                                  |Digikey    |
|Rp2040                   |motherboard                                          |1       |3.49            |https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/100045204/28959890                                                                                                    |Digikey    |
|Ec11 rotary encoder      |so i can change brightness of oled to prevent burn in|1       |1.47            |https://www.aliexpress.com/item/1005006693443387.html?mp=1&pdp_npi=6@dis!USD!USD%201.47!USD%200.99!!USD%200.99!!!@210328df17757913589444878e58cd!12000048311239365!ct!AU!7513952212!!1!0!|ali express|
|LM75AD,118               |Temperature sensor                                   |1       |0.71            |https://www.digikey.com/en/products/detail/nxp-usa-inc/LM75ADP-118/1156588                                                                                                               |Digikey    |
|PCB creating and shipping|For pcb                                              |1       |5.50            |                                                                                                                                                                                         |JLCPCB     |


Building the thing:
Once I recieved all the parts, I started soldering, I tried normally soldering the LM75AD sensor without flux, but the pads kept bridging, so I applied flux. Since I didn't/don't have a solder wick, it was slightly harder, but I seperated all the bridges by flicking the soldering iron in a way that broke the bridges. Once the sensor was soldered on, I moved on to the rotary encoder, it was pretty simple, but my soldering was pretty bad on it. Then, I moved on to the oled, with only 4 pins, it was really easy, I just had to make sure it was in the correct position before I soldered it. Next, I soldered the headers to the rp2040 and soldered it onto the PCB. This was my favourite part because I find it extremely satisfying to solder the pins on microcontrollers. Lastly, I soldered on the resistors. The resistors were kind of weird, because the hole distance is a lot smaller than the actual resistors, so I had to squeeze them in. Once I had finished soldering, I moved on to the code. I got my intitial code, uploaded it, uploaded the drivers or whatever its called and ran the code from thonny. Originally it didn't work becayse the oled screen was set to 64 as the y axis height instead of 32. Then I had to do some random other trouble shooting because the screen was upside down and some other stuff, but after a while, it finally worked.



https://github.com/user-attachments/assets/9b167287-3994-496b-82d9-43ea8c0a6dbe



https://github.com/user-attachments/assets/fa248c13-c449-4ee9-a2be-12438f792acb



https://github.com/user-attachments/assets/527572af-bf87-4742-be0e-cb3ad4938c7c



https://github.com/user-attachments/assets/440db2dd-6235-4dd3-aeeb-82b491f24ae7



https://github.com/user-attachments/assets/d056f70a-cc38-4e82-8550-2bf955608510



https://github.com/user-attachments/assets/0cdc1f9a-8a88-437c-a1f9-4a4462cc4919

<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 36 07" src="https://github.com/user-attachments/assets/882c2904-117a-434d-8cfa-7e1fa9fe9167" />
<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 36 07 (2)" src="https://github.com/user-attachments/assets/35bb93ab-fd39-4369-9b24-b09d26f4e4a5" />
<img width="2000" height="1500" alt="WhatsApp Image 2026-05-13 at 17 36 07 (1)" src="https://github.com/user-attachments/assets/6714c870-cae7-43e1-b95e-1d10522bf912" />
<img width="2048" height="1466" alt="WhatsApp Image 2026-05-13 at 17 36 06" src="https://github.com/user-attachments/assets/334d3009-7c12-42a3-95ec-399bbc13fbbc" />
<img width="1920" height="1536" alt="WhatsApp Image 2026-05-13 at 17 36 06 (1)" src="https://github.com/user-attachments/assets/7c775fcc-1a80-4be9-92ee-c35b67f69378" />
<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 36 05" src="https://github.com/user-attachments/assets/5e55421d-ddad-4f77-bd9a-54db4e4945de" />
<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 35 53" src="https://github.com/user-attachments/assets/895da207-2ac2-441a-aa14-45496550d7cd" />
<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 35 53 (2)" src="https://github.com/user-attachments/assets/e3e1a748-7658-4fc2-b85b-a675ddd0167f" />
<img width="1500" height="2000" alt="WhatsApp Image 2026-05-13 at 17 35 53 (1)" src="https://github.com/user-attachments/assets/36d32798-4892-4759-8d06-14f6e183f0dc" />
