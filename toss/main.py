import os, sys, doc
from optparse import OptionParser

def toss_main(argv=sys.argv[1:]):
    
    parser = OptionParser(
        usage="%prog [options]",
        version="%prog pre-alpha",
        add_help_option=False
    )
    
    parser.add_option(
        "-u", "--user", 
        dest="user",
        help="MySQL user name that is used to connect the server",
        type="string",
        default='root'
    )
    
    parser.add_option(
        "-p",
        dest="password",
        action="store_true"
    )
    
    parser.add_option(
        "--password", 
        dest="password",
        help="MySQL password that is used to connect the server",
        type="string",
        default=''
    )
    
    parser.add_option(
        "-P", "--port", 
        dest="port",
        help="MySQL port number to use for TCP/IP connection",
        type="int",
        default='3306'
    )
    
    parser.add_option(
        "-h", "--host", 
        dest="host",
        help="MySQL server host",
        type="string",
        default='127.0.0.1'
    )
    
    parser.add_option(
        "-D", "--database", 
        dest="database",
        help="Database should be used",
        type="string",
        default=None
    )
    
    parser.add_option(
        "--default-character-set", 
        dest="charset",
        help="character set used as default",
        type="string",
        default="utf8"
    )
    
    parser.add_option(
        "--help", "--usage", 
        action='help'
    )
    
    (options, args) = parser.parse_args()
    if options.password is True:
        options.password = raw_input('password:')
    
    """
        DEBUG
    """
    options.charset = 'utf8'
    options.database = 'kiki'
    options.host = '127.0.0.1'
    options.user = 'root'
    options.password = ''
    options.port = 3306
    
    doc.export(options=options, args=args)

if __name__ == '__main__': toss_main()