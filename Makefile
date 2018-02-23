all:
	git remote add resin whitaker@git.resin.io:whitaker/pialert.git

install:
	git push -f resin HEAD:master

clean:
	git remote rm resin