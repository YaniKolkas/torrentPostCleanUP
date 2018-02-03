import os
import shutil

extentions_subs = ['sub', 'srt']


def check_file_extention(file_name, extention):
    """"Function that check given filename extension is in the containing in the list passed as second argument"""

    if not file_name:
        raise ValueError('empty file name passed')

    if type(extention) is not list:
        raise ValueError('Passed extention is not list')

    if len(extention) == 0:
        raise ValueError('Passed extention list is  empty')

    if '.' in file_name:
        splitted_name = file_name.split('.')
        splitted_whitespace_name = filter(None, splitted_name)
        file_extention = splitted_whitespace_name[-1]
        return file_extention in extention
    else:
        return False


def check_dir_sub_or_empty(dirname):
    """"Function that is checking if given directory is empty or contains files only with sub extensions"""

    for root, dirs, files in os.walk(dirname):
        for found_file in files:
            file_is_sub = check_file_extention(found_file, extentions_subs)
            if not file_is_sub:
                return False

    return True


def main():
    """"main function for cleanning empty directories or dirs containing only subs"""

    top_dirs = [x for x in os.listdir('.') if os.path.isdir(x)]

    if not top_dirs:
        print "Not found any subdirs from current working directory {}".format(os.getcwd())
        print "Nothing left to do here"
        exit(0)

    print "Top dirs:"
    print top_dirs

    dirs_for_delete = [x for x in top_dirs if check_dir_sub_or_empty(x)]

    if not dirs_for_delete:
        print 'Not found any dirs for cleaning ...'
        print 'Gracefully exit ...'
        exit(0)

    print "dirs that need to be deleted:"
    for fdir in dirs_for_delete:
        print "\t{}".format(fdir)

    print "\n\nStart Deleting dir by dir:"
    for fdir in dirs_for_delete:
        print 'Attempting to delete {} ...'.format(fdir),
        shutil.rmtree(fdir, ignore_errors=True)
        print '  OK'


if __name__ == '__main__':
    main()
