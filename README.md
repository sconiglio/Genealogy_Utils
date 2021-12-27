This is a respository for various (simple) genealogy tools that are in the works.

  To use the Genealogy Record Indexer, make sure that you have (the latest version of) python installed (eventually this will not be a requirement).
  
    Upon usage, the program's console will open. The console will ask the user to provide the file location of a CSV file.
    The program includes three modes: marriage record indexing, birth record indexing, and death record indexing.
    The modes can be accessed by simply entering in an integer value. Marriage record indexing also provides two submodes: groom first indexing and bride first indexing.
    The difference between the two modes, is that groom first indexing enters in the groom's information first and bride first indexing enters in the bride's information first/
    
    Upon entering any of the three modes, the user will be able to select whether or not they would like to add a header. The selection will be made with either the entering of an integer, or nothing at all.
    Henceforth, the user is guided through entering the various information needed for a detailed CSV indexing. Once the user is done indexing, the user can type in BREAK to save the indexed information and close the program. If the user does not want to add a certain piece of data, the user can simply press ENTER to input a blank string.
    
    Heading layout for the different modes:
    Groom First Marriage Indexing: "Index_number", "Groom Name:", "Groom Birth Town:", "Bride Name:", "Bride Birth Town:", "Date:", "Groom Father:", "Groom Mother", "Bride Father:", "Bride Mother:", "Notes:"
    Bride First Marriage Indexing: "Bride Name:", "Bride Birth Town:", "Groom Name:", "Groom Birth Town", "Date:", "Bride Father:", "Bride Mother:", "Groom Father:", "Groom Mother", "Notes:"
    Death: "Date:", "Name", "Age", "Spouse:", "Birth town", "Father:", "Mother:", "Notes:"
    Birth: "Date:", "Name", "Father:", "Mother:", "Notes:"
