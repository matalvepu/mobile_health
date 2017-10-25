for f in ../data/data_20Oct_2017/*
do
	for file in $f/*.zip
		do
			unzip $file -d ${file::-4}/
			rm -f $file
		done
done