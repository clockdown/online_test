#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

BaseToChar={"000000":"A",	"010000":"Q",	"100000":"g",	"110000":"w",
			"000001":"B",	"010001":"R",	"100001":"h",	"110001":"x",
			"000010":"C",	"010010":"S",	"100010":"i",	"110010":"y",
			"000011":"D",	"010011":"T",	"100011":"j",	"110011":"z",
			"000100":"E",	"010100":"U",	"100100":"k",	"110100":"0",
			"000101":"F",	"010101":"V",	"100101":"l",	"110101":"1",
			"000110":"G",	"010110":"W",	"100110":"m",	"110110":"2",
			"000111":"H",	"010111":"X",	"100111":"n",	"110111":"3",
			"001000":"I",	"011000":"Y",	"101000":"o", 	"111000":"4",
			"001001":"J",	"011001":"Z",	"101001":"p",	"111001":"5",
			"001010":"K",	"011010":"a",	"101010":"q",	"111010":"6",
			"001011":"L",	"011011":"b",	"101011":"r",	"111011":"7",
			"001100":"M",	"011100":"c",	"101100":"s",	"111100":"8",
			"001101":"N",	"011101":"d",	"101101":"t",	"111101":"9",
			"001110":"O",	"011110":"e",	"101110":"u",	"111110":"+",
			"001111":"P",	"011111":"f",	"101111":"v",	"111111":"/"}

CharToBase={v:k for k, v in BaseToChar.items()}

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