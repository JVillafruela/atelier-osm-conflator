#awk 'BEGIN {FS="\t"} ; NR>1 {print $4} ' < pav.tsv
[ -d pav-communes ] || mkdir pav-communes
rm pav-communes/pav*.tsv
awk 'BEGIN {FS="\t";}
	(NR==1)	{header=$0}
	NR>1	{gsub(/ /,"-",$4); fname="pav-communes/pav-"  $4 ".tsv"
			nbl[$4]++ ; 
			if (nbl[$4]==1) {print header>fname}
			print > fname  }
	#END {print header }
' < pav.tsv