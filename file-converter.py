import sys
import os
import markdown

def read_file(filepath):  #ファイルの読み込み
  try:
    with open(filepath, 'r', encoding='utf-8') as file:
      return file.read()
  except FileNotFoundError:
    print("ファイルが見つかりません\n")
    return None

def judge_markdown(filepath) -> bool:
  '''markdownファイルかどうかを判定'''
  _, root_ext_pair = os.path.splitext(filepath)  #拡張子とそれ以外のタプルで返ってくる
  return root_ext_pair=='.md'

def judge_html(filepath):
  _, root_ext_pair = os.path.splitext(filepath)
  return root_ext_pair=='.html'

def write_file(filepath, contents):
  try:
    with open(filepath, 'w') as file:
      file.write(contents)
  except:
    print("ファイル名を指定してください。\n")


def main():
  args = sys.argv
  if len(args) < 4:
    print("コマンドが誤りです。再度入力してください\n")
    return
  command = args[1]
  inputpath = args[2]
  outputpath = args[3]
  if command != 'markdown':
    print("コマンドが誤りです。再度入力してください\n")
    return
  try:
    if judge_markdown(inputpath):
      html_output = markdown.markdown(read_file(inputpath))
    else:
      print("markdownファイルを指定してください\n")
      return
  except:
    print("ファイルが見つかりませんでした。\n")
    return

  try:
    if judge_html(outputpath):
      write_file(outputpath, html_output)
    else:
      print("markdownファイルを指定してください\n")
      return
  except:
    print("ファイルが見つかりませんでした。\n")
    return


if __name__ == '__main__':
  main()
