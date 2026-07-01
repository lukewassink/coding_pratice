# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory
# subdir2 containing a file file.ext.

# The string
# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1
# contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file
# file2.ext.

# We are interested in finding the longest (number of characters) absolute path
# to a file within our file system. For example, in the second example above,
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
# length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the
# length of the longest absolute path to a file in the abstracted file system.
# If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.


def longest_path(file_structure):
    max_path_length = 0
    cur_path_length = 0
    path_lengths = []
    
    depth = 0
    length = 0
    pos = 0

    while pos < len(file_structure):
        if file_structure[pos] == "\\":
            if file_structure[pos + 1] == "n":
                path_lengths.append(length + 1)
                cur_path_length += length + 1
                length = 0
                depth = 0
            else:
                depth += 1
            pos += 1
        else:
            while depth < len(path_lengths):
                cur_path_length -= path_lengths.pop()
            length += 1
            
        pos += 1
        
        if pos == len(file_structure):
            cur_path_length += length

        max_path_length = max(max_path_length, cur_path_length)

    return max_path_length

print(longest_path(r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
