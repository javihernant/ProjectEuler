import os

def count_digs(filename):
    i = 0
    while i < len(filename) and filename[i].isdigit():
        i+= 1
    return i

def max_num_digs():
    max_digs = 0
    for file in os.listdir("."):
        name, ext = os.path.splitext(file)
        if ext == ".py" and name[0].isdigit():
            digs_cnt = count_digs(name)
            if digs_cnt >max_digs:
                max_digs = digs_cnt
    return max_digs

def rename_files():
    max_digs = max_num_digs()
    rename_cnt = 0
    for file in os.listdir("."):
        name, ext = os.path.splitext(file)
        if ext == ".py" and name[0].isdigit():
            cnt_digs = count_digs(name)
            if cnt_digs < max_digs:
                old_name = name + ext
                new_name = "".zfill(max_digs - cnt_digs) + old_name
                print(file, "->", new_name)
                os.rename(old_name, new_name)
                rename_cnt += 1
    print(rename_cnt, "files were renamed")
                

    

def main():
    rename_files()

if __name__ == '__main__':
    main()
