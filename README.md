alert-me-when-this-site-goes-down
=================================

This script alert you when a site goes or slows down.

    $ python alertmewhenthissitegoesdown.py -h
    usage: alertmewhenthissitegoesdown.py [-h] [--timeout S] [--repeat S]
                                          [--times NUM]
                                          URL
    
    alertmewhenthissitegoesdown.py 0.1
    Alert me, when this site goes down.
    
    positional arguments:
      URL          url to check
    
    optional arguments:
      -h, --help   show this help message and exit
      --timeout S  timeout in S seconds (default: 10)
      --repeat S   check it again after S seconds (default: 60)
      --times NUM  alert only NUM times in a row (default: 3)
    
        Sample usage:
          python alertmewhenthissitegoesdown.py http://xxx.xxx/xxx.xxx 


![Screenshot](https://github.com/szeghybarna/alert-me-when-this-site-goes-down/raw/master/screenshot.png)

