#######################################################################@@#
# Smrečice
#######################################################################@@#

##################################################################@000297#
# 1) Petvrstično smrečico lahko v Pythonu izpišemo z naslednjim programom:
#
# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
#
# Sestavite program, ki izpiše osemvrstično smrečico.
##################################################################000297@#
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
print("********")
##################################################################@000298#
# 2) Program za izpis osemvrstične smrečice popravite tako, da namesto niza
# z $n$ zvezdicami '**...*' uporabite izraz n * '*', na primer namesto
# niza '*****' uporabite izraz 5 * '*'.
##################################################################000298@#
print(1*"*")
print(2*"*")
print(3*"*")
print(4*"*")
print(5*"*")
print(6*"*")
print(7*"*")
print(8*"*")
##################################################################@000300#
# 3) Osemvrstično smrečico izpišite z enim samim klicem funkcije print.
#
# *Namig*: znak za prelom vrstice je "\n".
##################################################################000300@#
#print(1*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*"\n 2*"*")
#print(1*"*" + "\n" + 2*"*" + "\n" 3*"*" + "\n" + 4*"*" + "\n" 5*"*" + "\n" + 6*"*" + "\n" 7*"*" + "\n" + 8*"*" )
print(1*"*" + "\n" + 2*"*" + "\n" + 3*"*" + "\n"  + 4*"*" + "\n"  + 5*"*" + "\n"  + 6*"*" + "\n"  + 7*"*" + "\n"  + 8*"*" )
##################################################################@000301#
# 4) Osemvrstično smrečico izpišite še desno poravnano.
# Na primer:
#
#     *
#    **
#   ***
#  ****
# *****
#
# *Namig*: na začetku vsake vrstice natisnite ustrezno število presledkov.
##################################################################000301@#
print(7*" " + 1*"*" + "\n" +6*" " + 2*"*" + "\n" +5*" " + 3*"*" + "\n"+4*" " + 4*"*" + "\n" + +3*" " + 5*"*"+"\n" +2*" " + 6*"*" + "\n" +1*" " + 7*"*" + "\n" +0*" " + 8*"*" )
##################################################################@000302#
# 5) Osemvrstično smrečico izpišite še sredinsko poravnano in z razmaki.
# Na primer:
#
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#
# *Namig*: levi rob je enak kot pri desno poravnani smrečici, za vsakim
# osnovnim znakom pa je presledek.
##################################################################000302@#
print(7*" " + 1*"* " +"\n"
      +6*" " + 2*"* "+"\n"
      +5*" " + 3*"* "+ "\n"
      +4*" " + 4*"* "+"\n"
      +3*" " + 5*"* " +"\n"
      +2*" " + 6*"* " +"\n"
      +1*" " + 7*"* " +"\n"
      +0*" " + 8*"* " )

print("\n     . . .\nČe vidiš ta text, pomeni, da internet DELA !!!\n     . . .\n")































































































#######################################################################@@#
# Kode pod to črto nikakor ne spreminjajte.
##########################################################################

"TA VRSTICA JE PRAVILNA."
"ČE VAM PYTHON SPOROČI, DA JE V NJEJ NAPAKA, SE MOTI."
"NAPAKA JE NAJVERJETNEJE V ZADNJI VRSTICI VAŠE KODE."
"ČE JE NE NAJDETE, VPRAŠAJTE ASISTENTA."



























































import io, json, os, re, sys, shutil, traceback
from contextlib import contextmanager
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
class Check:
    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['errors'] = []
            part['challenge'] = []
        Check.current = None
        Check.part_counter = None
        Check.user_id = 696

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current = Check.parts[Check.part_counter]
        return Check.current.get('solution', '').strip() != ''

    @staticmethod
    def error(msg, *args, **kwargs):
        Check.current['errors'].append(msg.format(*args, **kwargs))

    @staticmethod
    def challenge(x, k=""):
        pair = (str(k), str(Check.canonize(x)))
        Check.current['challenge'].append(pair)

    @staticmethod
    def execute(example, env={}, use_globals=True, do_eval=False, catch_exception=False):
        local_env = {}
        local_env.update(env)
        global_env = globals() if use_globals else {}
        old_stdout, old_stderr = sys.stdout, sys.stderr
        new_stdout, new_stderr = io.StringIO(), io.StringIO()
        exec_info = {'env': local_env}
        try:
            sys.stdout, sys.stderr = new_stdout, new_stderr
            if do_eval:
                exec_info['value'] = eval(example, global_env, local_env)
            else:
                exec(example, global_env, local_env)
        except Exception as e:
            if catch_exception:
                exec_info['exception'] = e
            else:
                raise e
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr
        exec_info['stdout'] = new_stdout.getvalue()
        exec_info['stderr'] = new_stderr.getvalue()
        return exec_info

    @staticmethod
    def run(example, state, message=None, env={}, clean=lambda x: x):
        code = "\n".join(example)
        example = "  >>> " + "\n  >>> ".join(example)
        s = {}
        s.update(env)
        exec (code, globals(), s)
        errors = []
        for (x,v) in state.items():
            if x not in s:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(s[x]) != clean(v):
                errors.append('morajo nastaviti {0} na {1},\nvendar nastavijo {0} na {2}'.format(x, v, s[x]))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', example,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    def canonize(x, digits=6):
        if   type(x) is float:
            x = round(x, digits)
            # We want to canonize -0.0 and similar small negative numbers to 0.0
            # Since -0.0 still behaves as False, we can use the following
            return x if x else 0.0
        elif type(x) is complex: return complex(Check.canonize(x.real, digits), Check.canonize(x.imag, digits))
        elif type(x) is list: return list([Check.canonize(y, digits) for y in x])
        elif type(x) is tuple: return tuple([Check.canonize(y, digits) for y in x])
        elif type(x) is dict: return sorted([(Check.canonize(k, digits), Check.canonize(v, digits)) for (k,v) in x.items()])
        elif type(x) is set: return sorted([Check.canonize(y, digits) for y in x])
        else: return x

    @staticmethod
    def equal(example, value=None, exception=None,
                clean=lambda x: x, env={},
                precision=1.0e-6, strict_float=False, strict_list=True):
        def difference(x, y):
            if x == y: return None
            elif (type(x) != type(y) and
                 (strict_float or not (type(y) in [int, float, complex] and type(x) in [int, float, complex])) and
                 (strict_list or not (type(y) in [list, tuple] and type(x) in [list, tuple]))):
                return "različna tipa"
            elif type(y) in [int, float, complex]:
                return ("numerična napaka" if abs(x - y) > precision else None)
            elif type(y) in [tuple,list]:
                if len(y) != len(x): return "napačna dolžina seznama"
                else:
                    for (u, v) in zip(x, y):
                        msg = difference(u, v)
                        if msg: return msg
                    return None
            elif type(y) is dict:
                if len(y) != len(x): return "napačna dolžina slovarja"
                else:
                    for (k, v) in y.items():
                        if k not in x: return "manjkajoči ključ v slovarju"
                        msg = difference(x[k], v)
                        if msg: return msg
                    return None
            else: return "različni vrednosti"

        local = locals()
        local.update(env)

        if exception:
            try:
                eval(example, globals(), local)
            except Exception as e:
                if e.__class__ != exception.__class__ or e.args != exception.args:
                    Check.error("Izraz {0} sproži izjemo {1!r} namesto {2!r}.",
                                example, e, exception)
                    return False
                else:
                    return True
            else:
                Check.error("Izraz {0} vrne {1!r} namesto da bi sprožil izjemo {2}.",
                            example, returned, exception)
                return False

        else:
            returned = eval(example, globals(), local)
            reason = difference(clean(returned), clean(value))
            if reason:
                Check.error("Izraz {0} vrne {1!r} namesto {2!r} ({3}).",
                            example, returned, value, reason)
                return False
            else:
                return False

    @staticmethod
    def generator(example, good_values, should_stop=False, further_iter=0, env={},
                  clean=lambda x: x, precision=1.0e-6, strict_float=False, strict_list=True):
        from types import GeneratorType

        def difference(x, y):
            if x == y: return None
            elif (type(x) != type(y) and
                    (strict_float or not (type(y) in [int, float, complex] and type(x) in [int, float, complex])) and
                    (strict_list or not (type(y) in [list, tuple] and type(x) in [list, tuple]))):
                return "različna tipa"
            elif type(y) in [int, float, complex]:
                return ("numerična napaka" if abs(x - y) > precision else None)
            elif type(y) in [tuple,list]:
                if len(y) != len(x): return "napačna dolžina seznama"
                else:
                    for (u, v) in zip(x, y):
                        msg = difference(u, v)
                        if msg: return msg
                    return None
            elif type(y) is dict:
                if len(y) != len(x): return "napačna dolžina slovarja"
                else:
                    for (k, v) in y.items():
                        if k not in x: return "manjkajoči ključ v slovarju"
                        msg = difference(x[k], v)
                        if msg: return msg
                    return None
            else: return "različni vrednosti"

        local = locals()
        local.update(env)
        gen = eval(example, globals(), local)
        if not isinstance(gen, GeneratorType):
            Check.error("{0} ni generator.", example)
            return False

        iter_counter = 0
        try:
            for correct_ans in good_values:
                iter_counter += 1
                student_ans = gen.__next__()
                reason = difference(clean(correct_ans), clean(student_ans))
                if reason:
                    Check.error("Element #{0}, ki ga vrne generator {1} ni pravilen: {2!r} namesto {3!r} ({4}).",
                                iter_counter, example, student_ans, correct_ans, reason)
                    return False
            for i in range(further_iter):
                iter_counter += 1
                gen.__next__() # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", example)
            return False

        if should_stop:
            try:
                gen.__next__()
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", example)
            except StopIteration:
                pass # this is fine
        return True

    @staticmethod
    @contextmanager
    def in_file(filename, content):
        with open(filename, "w") as _f:
            for line in content:
                print(line, file=_f)
        old_errors = Check.current["errors"][:]
        yield
        new_errors = Check.current["errors"][len(old_errors):]
        Check.current["errors"] = old_errors
        if new_errors:
            new_errors = ["\n    ".join(error.split("\n")) for error in new_errors]
            Check.error("Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}", filename, "\n  ".join(content), "\n- ".join(new_errors))

    @staticmethod
    def out_file(filename, content):
        with open(filename) as _f:
            out_lines = _f.readlines()
        len_out, len_given = len(out_lines), len(content)
        if len_out < len_given:
            out_lines += (len_given - len_out) * ["\n"]
        else:
            content += (len_out - len_given) * ["\n"]
        equal = True
        line_width = max(len(out_line.rstrip()) for out_line in out_lines + ["je enaka"])
        diff = []
        for out, given in zip(out_lines, content):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append("{0} {1} {2}".format(out.ljust(line_width), "|" if out == given else "*", given))
        if not equal:
            Check.error("Izhodna datoteka {0}\n je enaka{1}  namesto:\n  {2}", filename, (line_width - 7) * " ", "\n  ".join(diff))

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not part['solution'].strip():
                print('Podnaloga {0} je brez rešitve.'.format(i + 1))
            elif part['errors']:
                print('Podnaloga {0} ni prestala vseh testov:'.format(i + 1))
                for e in part['errors']:
                    print("- {0}".format("\n  ".join(e.splitlines())))
            elif 'rejection' in part:
                reason = ' ({0})'.format(part['rejection']) if part['rejection'] else ''
                print('Podnaloga {0} je zavrnjena.{1}'.format(i + 1, reason))
            else:
                print('Podnaloga {0} je pravilno rešena.'.format(i + 1))


def _check():
    _filename = os.path.abspath(sys.argv[0])
    with open(_filename, encoding='utf-8') as _f:
        _source = _f.read()

    Check.initialize([
        {
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in re.compile(
            r'#+@(?P<part>\d+)#\n' # beginning of header
            r'.*?'                 # description
            r'#+(?P=part)@#\n'     # end of header
            r'(?P<solution>.*?)'   # solution
            r'(?=\n#+@)',          # beginning of next part
            flags=re.DOTALL|re.MULTILINE
        ).finditer(_source)
    ])
    Check.parts[-1]['solution'] = Check.parts[-1]['solution'].rstrip()


    problem_match = re.search(
        r'#+@@#\n'           # beginning of header
        r'.*?'               # description
        r'#+@@#\n'           # end of header
        r'(?P<preamble>.*?)' # preamble
        r'(?=\n#+@)',        # beginning of first part
        _source, flags=re.DOTALL|re.MULTILINE)

    if not problem_match:
        print("NAPAKA: datoteka ni pravilno oblikovana")
        sys.exit(1)

    _preamble = problem_match.group('preamble')


    if Check.part():
        try:
            def izpis(source):
                import io, sys
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                exec(source)
                sys.stdout = old_stdout
                return new_stdout.getvalue()

            def preveriSmrecico(smrecica, levi, desni, dovoljeni):
                vrstice = smrecica.splitlines()
                if len(vrstice) != 8:
                    Check.error("Smrečica nima osmih vrstic.")
                for i in range(0, min(8, len(vrstice))):
                    vrstica = vrstice[i]
                    if not vrstica.startswith((levi[i] - 1) * " "):
                        Check.error("{0}. vrstica se ne začne na {1}. znaku.".format(i + 1, levi[i]))
                    if len(vrstica.rstrip()) != desni[i]:
                        Check.error("{0}. vrstica se ne konča na {1}. znaku.".format(i + 1, desni[i]))
                    znaki = vrstica.replace(" ", "")
                    if len(znaki) != i + 1:
                        Check.error("{0}. vrstica ni sestavljena iz {0} znakov.".format(i + 1))
                    if any(znak not in dovoljeni for znak in znaki):
                        Check.error("{0}. vrstica vsebuje nedovoljene znake.".format(i + 1))
                if len([znak for znak in dovoljeni if znak in smrecica]) > 1:
                    Check.error("Smrečica je sestavljena iz različnih dovoljenih znakov.")

            dovoljeni = "*.#$@oO+="
            znak = "*"
            preveriSmrecico(izpis(Check.current["solution"]), 8 * [0], range(1, 9), "*")
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}", "\n  ".join(traceback.format_exc().split("\n"))[:-2])


    if Check.part():
        try:
            def izpis(source):
                import io, sys
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                exec(source)
                sys.stdout = old_stdout
                return new_stdout.getvalue()

            def preveriSmrecico(smrecica, levi, desni, dovoljeni):
                vrstice = smrecica.splitlines()
                if len(vrstice) != 8:
                    Check.error("Smrečica nima osmih vrstic.")
                for i in range(0, min(8, len(vrstice))):
                    vrstica = vrstice[i]
                    if not vrstica.startswith((levi[i] - 1) * " "):
                        Check.error("{0}. vrstica se ne začne na {1}. znaku.".format(i + 1, levi[i]))
                    if len(vrstica.rstrip()) != desni[i]:
                        Check.error("{0}. vrstica se ne konča na {1}. znaku.".format(i + 1, desni[i]))
                    znaki = vrstica.replace(" ", "")
                    if len(znaki) != i + 1:
                        Check.error("{0}. vrstica ni sestavljena iz {0} znakov.".format(i + 1))
                    if any(znak not in dovoljeni for znak in znaki):
                        Check.error("{0}. vrstica vsebuje nedovoljene znake.".format(i + 1))
                if len([znak for znak in dovoljeni if znak in smrecica]) > 1:
                    Check.error("Smrečica je sestavljena iz različnih dovoljenih znakov.")

            dovoljeni = "*.#$@oO+="
            source=Check.current["solution"]
            preveriSmrecico(izpis(source), 8 * [0], range(1, 9), "*")
            if "**" in re.sub(r'#.*', '', source):
                Check.error("V programu nastopata dve zaporedni zvezdici.")
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}", "\n  ".join(traceback.format_exc().split("\n"))[:-2])


    if Check.part():
        try:
            def izpis(source):
                import io, sys
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                exec(source)
                sys.stdout = old_stdout
                return new_stdout.getvalue()

            def preveriSmrecico(smrecica, levi, desni, dovoljeni):
                vrstice = smrecica.splitlines()
                if len(vrstice) != 8:
                    Check.error("Smrečica nima osmih vrstic.")
                for i in range(0, min(8, len(vrstice))):
                    vrstica = vrstice[i]
                    if not vrstica.startswith((levi[i] - 1) * " "):
                        Check.error("{0}. vrstica se ne začne na {1}. znaku.".format(i + 1, levi[i]))
                    if len(vrstica.rstrip()) != desni[i]:
                        Check.error("{0}. vrstica se ne konča na {1}. znaku.".format(i + 1, desni[i]))
                    znaki = vrstica.replace(" ", "")
                    if len(znaki) != i + 1:
                        Check.error("{0}. vrstica ni sestavljena iz {0} znakov.".format(i + 1))
                    if any(znak not in dovoljeni for znak in znaki):
                        Check.error("{0}. vrstica vsebuje nedovoljene znake.".format(i + 1))
                if len([znak for znak in dovoljeni if znak in smrecica]) > 1:
                    Check.error("Smrečica je sestavljena iz različnih dovoljenih znakov.")

            dovoljeni = "*.#$@oO+="
            source = Check.current["solution"]
            preveriSmrecico(izpis(source), 8 * [0], range(1, 9), dovoljeni)
            if re.sub(r'#.*', '', source).count("print(") > 1:
                Check.error("Program vsebuje več kot en klic funkcije print.")
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}", "\n  ".join(traceback.format_exc().split("\n"))[:-2])


    if Check.part():
        try:
            def izpis(source):
                import io, sys
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                exec(source)
                sys.stdout = old_stdout
                return new_stdout.getvalue()

            def preveriSmrecico(smrecica, levi, desni, dovoljeni):
                vrstice = smrecica.splitlines()
                if len(vrstice) != 8:
                    Check.error("Smrečica nima osmih vrstic.")
                for i in range(0, min(8, len(vrstice))):
                    vrstica = vrstice[i]
                    if not vrstica.startswith((levi[i] - 1) * " "):
                        Check.error("{0}. vrstica se ne začne na {1}. znaku.".format(i + 1, levi[i]))
                    if len(vrstica.rstrip()) != desni[i]:
                        Check.error("{0}. vrstica se ne konča na {1}. znaku.".format(i + 1, desni[i]))
                    znaki = vrstica.replace(" ", "")
                    if len(znaki) != i + 1:
                        Check.error("{0}. vrstica ni sestavljena iz {0} znakov.".format(i + 1))
                    if any(znak not in dovoljeni for znak in znaki):
                        Check.error("{0}. vrstica vsebuje nedovoljene znake.".format(i + 1))
                if len([znak for znak in dovoljeni if znak in smrecica]) > 1:
                    Check.error("Smrečica je sestavljena iz različnih dovoljenih znakov.")

            dovoljeni = "*.#$@oO+="
            source = Check.current["solution"]
            preveriSmrecico(izpis(source), range(7, -1, -1), 8 * [8], dovoljeni)
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}", "\n  ".join(traceback.format_exc().split("\n"))[:-2])


    if Check.part():
        try:
            def izpis(source):
                import io, sys
                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout
                exec(source)
                sys.stdout = old_stdout
                return new_stdout.getvalue()

            def preveriSmrecico(smrecica, levi, desni, dovoljeni):
                vrstice = smrecica.splitlines()
                if len(vrstice) != 8:
                    Check.error("Smrečica nima osmih vrstic.")
                for i in range(0, min(8, len(vrstice))):
                    vrstica = vrstice[i]
                    if not vrstica.startswith((levi[i] - 1) * " "):
                        Check.error("{0}. vrstica se ne začne na {1}. znaku.".format(i + 1, levi[i]))
                    if len(vrstica.rstrip()) != desni[i]:
                        Check.error("{0}. vrstica se ne konča na {1}. znaku.".format(i + 1, desni[i]))
                    znaki = vrstica.replace(" ", "")
                    if len(znaki) != i + 1:
                        Check.error("{0}. vrstica ni sestavljena iz {0} znakov.".format(i + 1))
                    if any(znak not in dovoljeni for znak in znaki):
                        Check.error("{0}. vrstica vsebuje nedovoljene znake.".format(i + 1))
                if len([znak for znak in dovoljeni if znak in smrecica]) > 1:
                    Check.error("Smrečica je sestavljena iz različnih dovoljenih znakov.")

            dovoljeni = "*.#$@oO+="
            source = Check.current["solution"]
            preveriSmrecico(izpis(source), range(7, -1, -1), range(8, 17), dovoljeni)
            pass
        except:
            Check.error("Testi sprožijo izjemo\n  {0}", "\n  ".join(traceback.format_exc().split("\n"))[:-2])




    print('Shranjujem rešitve na strežnik... ', end = "")
    post = json.dumps({
        'data': '{"timestamp": "2013-07-22 14:28:58.013459+00:00", "problem": 97, "user": 696}',
        'signature': 'b59565e29d7c1e7567f917e1f3d91fa0',
        'preamble': _preamble,
        'attempts': Check.parts,
        'source': _source,
    }).encode('utf-8')
    try:
        r = urlopen('http://tomo.fmf.uni-lj.si:80/problem/upload/student/', post)
        response = json.loads(r.read().decode('utf-8'))
        print('Rešitve so shranjene.')
        for (k, e) in response['rejected']:
            Check.parts[k - 1]['rejection'] = e
        Check.summarize()
        if 'update' in response:
            print("Posodabljam datoteko... ", end = "")
            index = 1
            while os.path.exists('{0}.{1}'.format(_filename, index)):
                index += 1
            backup_filename = "{0}.{1}".format(_filename, index)
            shutil.copy(_filename, backup_filename)
            r = urlopen(response['update'])
            with open(_filename, 'w', encoding='utf-8') as _f:
                _f.write(r.read().decode('utf-8'))
            print("Stara datoteka je preimenovana v {0}.".format(os.path.basename(backup_filename)))
            print("Če se datoteka v urejevalniku ni osvežila, jo zaprite ter ponovno odprite.")
    except HTTPError as r:
        print('Pri shranjevanju je prišlo do napake.')
        Check.summarize()
        print('Pri shranjevanju je prišlo do napake. Poskusite znova.')
        Check.error = r.read().decode('utf-8')


_check()

#####################################################################@@#
