show:
	for f in output/*; do echo $$f; echo ---; cat $$f; echo ---; done
