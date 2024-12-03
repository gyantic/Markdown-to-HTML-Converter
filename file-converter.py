import sys
import os
import markdown

def read_file(filepath):  #ファイルの読み込み
  try:
    with open(filepath, 'r', encoding='utf-8') as file:
      return file.read()
  except:
    print("ファイルが見つかりません\n")
    return None

def judge_extension(filepath) -> bool:
  '''markdownファイルかどうかを判定'''
  root_ext_pair = os.path.splitext(filepath)
  return root_ext_pair=='.md'

def main():
  args = sys.argv
  if len(args) < 4:
    print("コマンドが誤りです。再度入力してください\n")
    return
  command = args[1]
  inputpath = 
  if command != 'Markdown':
    print("コマンドが誤りです。再度入力してください\n")
  try:
    if judge_extension(arg)
