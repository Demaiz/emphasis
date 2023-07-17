from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, AuthenticationUserForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import json as js


def index(request):
    # I use code below to add words to db

    # words = Words()
    # d = ['Агроно́мія', 'Алфа́ві́т', 'А́ркушик', 'Асиметрі́я', 'Багаторазо́вий', 'Безпринци́пний', 'Бе́шкет', 'Бла́говіст', 'Близьки́й', 'Болоти́стий', 'Боро́давка', 'Босо́ніж', 'Боя́знь', 'Бурштино́вий', 'Бюлете́нь', 'Ва́ги (у множині)', 'Вантажі́вка', 'Весня́ни́й', 'Ви́года (користь)', 'Виго́да (зручність)', 'Вида́ння', 'Визво́льний', 'Вимо́га', 'Ви́падок', 'Вира́зний', 'Ви́сіти', 'Ви́трата', 'Виши́ваний', 'Відвезти́', 'Відвести́', 'Ві́дгомін', 'Віднести́', 'Ві́домість (список)', 'Відо́мість (повідомлення, дані, популярність)', 'Ві́рші', 'Віршови́й', 'Вітчи́м', 'Гальмо́, га́льма', 'Гляда́ч', 'Гороши́на', 'Граблі́', 'Гурто́житок', 'Дани́на', 'Да́но', 'Дециме́тр', 'Де́щиця', 'Де-ю́ре', 'Джерело́', 'Ди́влячись', 'Дича́віти', 'Діало́г', 'Добови́й', 'Добу́ток', 'Довезти́', 'Довести́', 'Дові́дник', 'До́гмат', 'Донести́', 'До́нька', 'Дочка́', 'Дро́ва', 'Експе́рт', 'Єрети́к', 'Жалюзі́', 'Завда́ння', 'Завезти́', 'Завести́', 'За́вжди́', 'Завчасу́', 'За́гадка', 'Заіржа́вілий', 'Заіржа́віти', 'Закінчи́ти', 'За́кладка (у книзі)', 'За́крутка', 'Залиши́ти', 'Замі́жня', 'Занести́', 'За́понка', 'Заробі́ток', 'За́ставка', 'За́стібка', 'Засто́порити', 'Зви́сока', 'Зда́лека', 'Зібра́ння', 'Зобрази́ти', 'Зо́зла', 'Зра́ння', 'Зру́чний', 'Зубо́жіння', 'Інду́стрія', 'Ка́мбала', 'Катало́г', 'Кварта́л', 'Ки́шка', 'Кіломе́тр', 'Кінчи́ти', 'Ко́лесо', 'Ко́лія', 'Ко́пчений (дієприкметник)', 'Копче́ний (прикметник)', 'Кори́сний', 'Ко́сий', 'Котри́й', 'Крице́вий', 'Кро́їти', 'Кропива́', 'Куліна́рія', 'Ку́рятина', 'Ла́те', 'Листопа́д', 'Літо́пис', 'Лю́стро', 'Ма́бу́ть', 'Магісте́рський', 'Ма́ркетинг', 'Мере́жа', 'Металу́ргія', 'Міліме́тр', 'Навча́ння', 'Нанести́', 'Напі́й', 'На́скрізний', 'На́чинка', 'Нена́видіти', 'Нена́висний', 'Нена́висть', 'Нести́', 'Ні́здря', 'Нови́й', 'Обіця́нка', 'Обра́ння', 'Обру́ч (іменник)', 'Одина́дцять', 'Одноразо́вий', 'Озна́ка', 'О́лень', 'Опто́вий', 'Осете́р', 'Ота́ман', 'О́цет', 'Пави́ч', 'Парте́р', 'Пе́карський', 'Перевезти́', 'Перевести́', 'Пере́кис', 'Переля́к', 'Перенести́', 'Пере́пад', 'Пере́пис', 'Піала́', 'Пі́дданий (дієприкметник)', 'Підда́ний (іменник, істота)', 'Пі́длітковий', 'Пізна́ння', 'Пітни́й', 'Піце́рія', 'По́друга', 'По́значка', 'По́ми́лка', 'Помі́щик', 'Помо́вчати', 'Поня́ття', 'Порядко́вий', 'Посере́дині', 'Привезти́', 'Привести́', 'При́морозок', 'Принести́', 'При́чіп', 'Про́діл', 'Промі́жок', 'Псевдоні́м', 'Ра́зом', 'Ре́мінь (пояс)', 'Ре́шето', 'Ри́нковий', 'Рівни́на', 'Роздрібни́й', 'Ро́зпірка', 'Руко́пис', 'Русло́', 'Сантиме́тр', 'Све́рдло', 'Сере́дина', 'Се́ча', 'Симетрі́я', 'Сільськогоспода́рський', 'Сімдеся́т', 'Сли́на', 'Соломи́нка', 'Ста́туя', 'Стовідсо́тковий', 'Стриба́ти', 'Текстови́й', 'Течія́', 'Ти́гровий', 'Тисо́вий', 'Тім’яни́й', 'Травесті́я', 'Тризу́б', 'Ту́луб', 'Украї́нський', 'Уподо́бання', 'Урочи́стий', 'Усере́дині', 'Фарту́х', 'Фахови́й', 'Фено́мен', 'Фо́льга', 'Фо́рзац', 'Ха́ос (у міфології: стихія)', 'Хао́с (безлад)', 'Ца́рина', 'Цеме́нт', 'Це́нтнер', 'Цінни́к', 'Чарівни́й', 'Чергови́й', 'Чита́ння', 'Чорно́зем', 'Чорно́слив', 'Чотирна́дцять', 'Шляхопрові́д', 'Шовко́вий', 'Шофе́р', 'Ще́лепа', 'Щи́пці', 'Щодобови́й', 'Ярмарко́вий']
    # p = ['Агрономія', 'Алфавіт', 'Аркушик', 'Асиметрія', 'Багаторазовий', 'Безпринципний', 'Бешкет', 'Благовіст', 'Близький', 'Болотистий', 'Бородавка', 'Босоніж', 'Боязнь', 'Бурштиновий', 'Бюлетень', 'Ваги (у множині)', 'Вантажівка', 'Весняний', 'Вигода (користь)', 'Вигода (зручність)', 'Видання', 'Визвольний', 'Вимога', 'Випадок', 'Виразний', 'Висіти', 'Витрата', 'Вишиваний', 'Відвезти', 'Відвести', 'Відгомін', 'Віднести', 'Відомість (список)', 'Відомість (повідомлення, дані, популярність)', 'Вірші', 'Віршовий', 'Вітчим', 'Гальмо, гальма', 'Глядач', 'Горошина', 'Граблі', 'Гуртожиток', 'Данина', 'Дано', 'Дециметр', 'Дещиця', 'Де-юре', 'Джерело', 'Дивлячись', 'Дичавіти', 'Діалог', 'Добовий', 'Добуток', 'Довезти', 'Довести', 'Довідник', 'Догмат', 'Донести', 'Донька', 'Дочка', 'Дрова', 'Експерт', 'Єретик', 'Жалюзі', 'Завдання', 'Завезти', 'Завести', 'Завжди', 'Завчасу', 'Загадка', 'Заіржавілий', 'Заіржавіти', 'Закінчити', 'Закладка (у книзі)', 'Закрутка', 'Залишити', 'Заміжня', 'Занести', 'Запонка', 'Заробіток', 'Заставка', 'Застібка', 'Застопорити', 'Звисока', 'Здалека', 'Зібрання', 'Зобразити', 'Зозла', 'Зрання', 'Зручний', 'Зубожіння', 'Індустрія', 'Камбала', 'Каталог', 'Квартал', 'Кишка', 'Кілометр', 'Кінчити', 'Колесо', 'Колія', 'Копчений (дієприкметник)', 'Копчений (прикметник)', 'Корисний', 'Косий', 'Котрий', 'Крицевий', 'Кроїти', 'Кропива', 'Кулінарія', 'Курятина', 'Лате', 'Листопад', 'Літопис', 'Люстро', 'Мабуть', 'Магістерський', 'Маркетинг', 'Мережа', 'Металургія', 'Міліметр', 'Навчання', 'Нанести', 'Напій', 'Наскрізний', 'Начинка', 'Ненавидіти', 'Ненависний', 'Ненависть', 'Нести', 'Ніздря', 'Новий', 'Обіцянка', 'Обрання', 'Обруч (іменник)', 'Одинадцять', 'Одноразовий', 'Ознака', 'Олень', 'Оптовий', 'Осетер', 'Отаман', 'Оцет', 'Павич', 'Партер', 'Пекарський', 'Перевезти', 'Перевести', 'Перекис', 'Переляк', 'Перенести', 'Перепад', 'Перепис', 'Піала', 'Підданий (дієприкметник)', 'Підданий (іменник, істота)', 'Підлітковий', 'Пізнання', 'Пітний', 'Піцерія', 'Подруга', 'Позначка', 'Помилка', 'Поміщик', 'Помовчати', 'Поняття', 'Порядковий', 'Посередині', 'Привезти', 'Привести', 'Приморозок', 'Принести', 'Причіп', 'Проділ', 'Проміжок', 'Псевдонім', 'Разом', 'Ремінь (пояс)', 'Решето', 'Ринковий', 'Рівнина', 'Роздрібний', 'Розпірка', 'Рукопис', 'Русло', 'Сантиметр', 'Свердло', 'Середина', 'Сеча', 'Симетрія', 'Сільськогосподарський', 'Сімдесят', 'Слина', 'Соломинка', 'Статуя', 'Стовідсотковий', 'Стрибати', 'Текстовий', 'Течія', 'Тигровий', 'Тисовий', 'Тім’яний', 'Травестія', 'Тризуб', 'Тулуб', 'Український', 'Уподобання', 'Урочистий', 'Усередині', 'Фартух', 'Фаховий', 'Феномен', 'Фольга', 'Форзац', 'Хаос (у міфології: стихія)', 'Хаос (безлад)', 'Царина', 'Цемент', 'Центнер', 'Цінник', 'Чарівний', 'Черговий', 'Читання', 'Чорнозем', 'Чорнослив', 'Чотирнадцять', 'Шляхопровід', 'Шовковий', 'Шофер', 'Щелепа', 'Щипці', 'Щодобовий', 'Ярмарковий']
    #
    # for i in range(0, len(d)):
    #     objs = Words.objects.bulk_create([
    #     Words(words_emphasis=d[i], words_without_emphasis=p[i]),
    # ])

    return render(request, "emphasis/index.html")


def words(request):
    w = Words.objects.all()
    context = {
        "w": w
    }
    return render(request, "emphasis/words.html", context)


def play(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        # send words to js
        if request.method == 'GET':
            context = list(Words.objects.all().values())
            return JsonResponse({'context': context, "is_authenticated": request.user.is_authenticated})
        # receive statistic data
        if request.method == 'POST':
            data = js.loads(request.POST.get('url'))

            # send statistic data to data base
            a = get_object_or_404(User, pk=request.user.id)
            u, created = Statistic.objects.get_or_create(user_id=request.user.id)
            u.all_mistakes += data["wrong_answer"]
            u.all_right += data["right_answer"]
            u.user = a
            u.save()

            # send information about mistakes to database

            for value in data["words_with_mistake"]:
                # if user don't made a mistake in this word before add it to database
                obj, created = Mistakes.objects.get_or_create(user_id=request.user.id, word_mistakes=value,
                                                              defaults={"word_mistakes_counter": "3"})

                # if user made a mistake in this word again reset word_mistakes_counter
                if not created:
                    Mistakes.objects.filter(user_id=request.user.id, word_mistakes=value).update(
                        word_mistakes_counter=3)

            # update word_mistakes_counter if user give right answer

            for i in data["words_without_mistake"]:
                if Mistakes.objects.filter(word_mistakes=i, user_id=request.user.id).exists():
                    counter = \
                    Mistakes.objects.filter(word_mistakes=i, user_id=request.user.id).values("word_mistakes_counter")[
                        0]['word_mistakes_counter']
                    counter -= 1
                    if counter == 0:
                        Mistakes.objects.filter(word_mistakes=i, user_id=request.user.id).delete()
                    else:
                        Mistakes.objects.filter(word_mistakes=i, user_id=request.user.id).update(
                            word_mistakes_counter=counter)
            response_data = {'result': 'success'}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'result': 'error'})
    else:
        return render(request, "emphasis/play.html")


def mistakes(request):
    if request.user.is_authenticated:
        # get information about user mistakes
        m = Mistakes.objects.filter(user_id=request.user.id).values("word_mistakes", "word_mistakes_counter")
        context = {
            "m": m
        }
        return render(request, "emphasis/mistakes.html", context)
    else:
        return render(request, "emphasis/mistakes.html", )


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "emphasis/register.html"
    success_url = reverse_lazy("emphasis:index")

    def form_valid(self, form):
        user = form.save()
        # auto login
        login(self.request, user)
        return redirect("emphasis:index")


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = "emphasis/loginuser.html"

    def get_success_url(self):
        return reverse_lazy("emphasis:index")


def logout_user(request):
    logout(request)
    return redirect("emphasis:login")


def profile(request, username):
    get_user = get_object_or_404(User, username=username)

    # check if user play 1 or more times
    try:
        # get user statistic data
        user_data = Statistic.objects.filter(user_id=get_user.id).first()

        context = {
            "all_right": user_data.all_right,
            "all_mistakes": user_data.all_mistakes,
            "username": get_user.username,
        }
    # if not - results is 0
    except:
        context = {
            "all_right": 0,
            "all_mistakes": 0,
            "username": get_user.username,
        }

    return render(request, "emphasis/profile.html", context)
