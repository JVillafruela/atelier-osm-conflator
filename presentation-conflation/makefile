all: atelier-2019-12-09.html atelier-2019-04-08.html  atelier-2020-02-11.html

atelier-2020-02-11.html : atelier-2020-02-11.md
	pandoc  -t slidy -i -s --self-contained --highlight-style pygments -s atelier-2020-02-11.md -o atelier-2020-02-11.html 

atelier-2019-12-09.html : atelier-2019-12-09.md
	pandoc -f markdown_github -t slidy -i -s --self-contained --highlight-style pygments -s atelier-2019-12-09.md -o atelier-2019-12-09.html 

atelier-2019-04-08.html : atelier-2019-04-08.md
	pandoc -f markdown -t slidy -i -s --self-contained --highlight-style pygments -s atelier-2019-04-08.md -o atelier-2019-04-08.html 

conflation.html : conflation.md
	pandoc -f markdown -t slidy -i -s --self-contained --highlight-style pygments -s conflation.md -o conflation.html 


test.html : test.md
	pandoc -f markdown -t slidy -i -s --self-contained -s test.md -o test.html 



