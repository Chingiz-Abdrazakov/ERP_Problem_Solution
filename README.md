# ERP_Problem_Solution
Problem: Реализуйте механизм рекомендаций. Например, при указании желаемого времени и числа людей - рекомендовать пользователю подходящие помещения.
-----------------------------------------------------------------------------------------
File: solution.py

Type: Console application
-----------------------------------------------------------------------------------------
Description: Программа реализует бронирование помещений на следующий день в соответствии с желаниями пользователя.
Пользователь запускает программу, создается БД учетных записей. Предлагается зарегистрироваться или войти (для регистрации нажать 'u', для входа -- 'i').
Далее пользователь вводит свои данные, если возникают какие-то ошибки (например, пользователь хочет войти, а такого имени еще нет или пароль недостаточно сложный), то дается еще 2 попытки. Если после них все плохо, снова предлагается зарегистрироваться или войти. Если все ОК, то есть опции забронировать комнату (нажать 'b') или посмотреть список своих броней (нажать 's'), также есть опция выйти (нажать 'l').
Если пользователь жмет бронировать, то ему предлагается ввести желаемое время брони и количество людей. В соответствии с этим выдается список доступных переговорных. Далее программа бежит по массиву этих комнат (которые отсортированы в порядке возрастания вместимости для оптимизации) и предлагает забронировать ('y') или пойти дальше ('n'). Если все комнаты оказались неподходящими, предлагается просмотреть их еще раз или выйти.
