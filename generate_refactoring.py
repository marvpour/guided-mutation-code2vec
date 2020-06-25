import os,random
from shutil import copyfile
from refactoring_methods import *


def generate_adversarial(k, path, code, file_name):
        final_refactor = ''
        function_list = []
        class_name = ''

        Class_list, raw_code =  extract_class(code)

        for class_name in Class_list:
            function_list, class_name = extract_function(class_name)

        refac = []
        for func in function_list:
            refactored_code = func

            for t in range(k):
                refactors_list = [rename_argument, return_optimal, add_argumemts,enhance_for_loop,enhance_filed,enhance_if,rename_api,
                                    rename_local_variable,add_local_variable,rename_method_name,add_print]#
                refactor       = random.choice(refactors_list)

                try:
                    refactored_code = refactor(refactored_code)

                except Exception as error:
                    refactored_code = refactored_code
                    print('error:\t',error)

            refac.append(refactored_code)
        code_body = raw_code.strip() + ' ' + class_name.strip()

        for i in range(len(refac)):
            final_refactor = code_body.replace('vesal'+ str(i), str(refac[i]))
            code_body = final_refactor


        return final_refactor


if __name__ == '__main__':
    try:
        K = 5
        # i= 0

        mode = 'training/' # Options: training, test
        # new = 'new/'
        # dest_foler = '/Users/Vesal/Desktop/java-small/test/'
        dest_foler = '/Users/Vesal/Desktop/final_data/'
        # source = '/Users/Vesal/Desktop/vvv/'
        source = '/Users/Vesal/Desktop/java-large/'
        o = count = 0

        # open_file = open(source,'r')
        # code = open_file.read()
        # generate_adversarial(K, source, code, 'ProductSchemaDemo.java')
        print(source + mode)
        for path, d, file_names in os.walk(source + mode):
            if filename != '/Users/Vesal/Desktop/java-large/training/aphyr__clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/checkouts/clj-antlr/demo/src/java/EdnListener.java':
                for filename in file_names:
                    # print(filename)
                    if '.java' in filename:
                        # if 'new_' in filename:
                            # new = 'new_'
                        #     correct_name = "".join(filename.rsplit(new))
                        #     copyfile(path +'/'+ filename, source + mode + dest_foler + '/' + correct_name)

                        print(filename)
                        copyfile(path +'/'+ filename, dest_foler + mode + filename)
                        o += 1
                        # i += 1
                        # print(i)
                        # # os.rename(path +'/'+ filename, source + mode + '/' + filename)
                        try:
                            open_file = open(path +'/'+ filename,'r', encoding = 'ISO-8859-1')
                            code = open_file.read()
                            new_code = generate_adversarial(K, path, code, filename)

                            # wr_path = dest_foler + mode + 'new/' + filename
                            wr_path = dest_foler + mode + 'new_' + filename

                            if new_code is not '':
                                count += 1
                                l = open(wr_path,'w')
                                l.write(new_code)

                            else:
                                l = open(wr_path,'w')
                                l.write(code)

                        except Exception as error:
                            l = open(wr_path,'w')
                            l.write(code)

        print('done with for')
        print('Total copied files:', j)
        print('Total refactored files:', count)

    except OSError as exc:
        if exc.errno == 36:
            handle_filename_too_long()
        else:
            handle_filename_too_long()


        print('Im done handling too long name')
        print('Till NOW:')
        print('Total copied files:', j)
        print('Total refactored files:', count)
