ps aux | awk '{print $1}' | awk '
	{ names[$1] += 1 } 
END {
	for (name in names) {}
		print names[name], name
	}
}' | sort -rn | head
