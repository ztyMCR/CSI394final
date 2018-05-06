# CSI394final documentation

There are 4 folders

1. RWV1:
        RWV1_final can produced the sampled image as rwv1output.ppm
            a.read ppm
            b.average horizontally
            c.average vertically
            d.print rwv1
        RWV1inverse_final can turn rwv1 back to the original image
            a.read rwv1
            b.unfold vertically
            c.unfold hrorizontally
            d.print ppm
  
2. RLE:
        RLE: encode rle
        RLE: decode rle

3.Steganography:
        encryption:  read ppm, print encode.ppm
        decryption:  read original ppm and read encode.ppm , print the message
4. Final Project(conversation twitter bot):
        import tweepy , chatter bot
        train the bot
        connect to twitter account and read the first timeline from target accout
        generate response
        if catch duplicate
        throw a new topic from trend
        sleep for a while
        
