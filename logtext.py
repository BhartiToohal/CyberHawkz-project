print('''
	 oooooooooo.  oooo                               .    o8o       ooooooooooooo                     oooo                  oooo  
        ` 888'   `Y8b `888                             .o8    `"'       8'   888   `8                     `888                  `888  
          888     888  888 .oo.    .oooo.   oooo d8b .o888oo oooo            888       .ooooo.   .ooooo.   888 .oo.    .oooo.    888  
          888oooo888'  888P"Y88b  `P  )88b  `888""8P   888   `888            888      d88' `88b d88' `88b  888P"Y88b  `P  )88b   888  
          888    `88b  888   888   .oP"888   888       888    888            888      888   888 888   888  888   888   .oP"888   888  
          888    .88P  888   888  d8(  888   888       888 .  888            888      888   888 888   888  888   888  d8(  888   888  
         o888bood8P'  o888o o888o `Y888""8o d888b      "888" o888o          o888o     `Y8bod8P' `Y8bod8P' o888o o888o `Y888""8o o888o ''')
with open("website.log","r") as f:
                              lines=f.readlines()
                              with open("output.txt","w+") as nf:
                                                                for line in lines:
                                                                                 line=line.split(" ")
                                                                                 nf.write("IP \t\t Datetime \t\Timezone \t request Type \t\t\t\tPath \t\t Http protocol \t Status code \tPacket size \t\t User Info\n")
                                                                                 nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t\n".format(str(line[0]).replace('",',' '),str(line[3]).replace('",',' '),str(line[4]).replace('",',' '),str(line[5]).replace('"',' '),str(line[6]).replace('"',' '),str(line[7]).replace('",',' '),str(line[8]).replace('"',' '),str(line[9]).replace('"',' '),str(line[11:]).replace('"',' ')))
                                                                                          
                                                
