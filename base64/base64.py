#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.option('-i', 'intxt')
@click.option('-o', 'outtxt')
@click.option('-e', 'type', flag_value="encode", default=True)
@click.option('-d', 'type', flag_value="decode")
def cmd(intxt="", outtxt="", type="encode"):
    if not (intxt and outtxt):
    	raise click.BadParameter('-i [FILENAME] and -o [FILENAME] is')
    elif type == "decode":
    	decode(intxt, outtxt)
    else:
    	encode(intxt, outtxt)

def encode(inf, outf):
	""" 慣れ親しんだ文字列 to Base64のエンコードだオラァ！
		param inf : input file path
		param outf: output file path
	"""
	with open(inf) as f:
		data = f.read()
	ascii_data = [format(ord(x),'b').zfill(8) for x in data]
	ascii_s = ''.join(ascii_data)
	v = [ascii_s[i:i+6] for i in range(0, len(ascii_s), 6)]
	v[len(v)-1] = v[len(v)-1] + ("0" * (6 - len(v[len(v)-1])))
	base = [BaseToChar[x] for x in v]
	con = ''.join(base)
	fin = [con[i:i+4] for i in range(0, len(con), 4)]
	fin[len(fin)-1] = fin[len(fin)-1] + ("=" * (4 - len(fin[len(fin)-1])))
	out = ''.join(fin)
	with open(outf, 'w') as f:
		f.write(out)
	print(out)

def decode(inf, outf):
	""" Base64 to 慣れ親しんだ文字列のデコードだオラァ！
		param inf : input file path
		param outf: output file path
	"""
	with open(inf) as f:
		data = f.read()
	data = data.replace('=', '')
	s_list = list(data)
	bit=[CharToBase[x] for x in s_list]
	num = ''.join(bit)
	asciis = [num[i:i+8] for i in range(0, len(num), 8)]
	sentence = [chr(int(x,2)) for x in asciis]
	out = ''.join(sentence)
	with open(outf, 'w') as f:
		f.write(out)
	print(out)

def main():
	cmd()

if __name__ == '__main__':
    main()