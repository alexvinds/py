# HL7v2 to FHIR Integration Pipeline

## Описание проекта
Интеграционный пайплайн для преобразования медицинских данных из формата HL7v2.5.1 в FHIR R4 для дата-платформы на базе Aidbox.

## Архитектурное решение

### Вариант 1: Batch Processing Pipeline (рекомендуемый для текущих требований)

```
[EHR Systems] → [HL7v2 Messages] → [Apache Kafka] → [Spring Boot App] → [FHIR Validator] → [Aidbox Storage]
     ↓              ↓                    ↓              ↓              ↓              ↓
  Meditech      HL7v2.5.1          Kafka Topics    Spring Boot    FHIR R4       Aidbox
  Epic          Messages            (3 partitions)  Microservice  Validation    Database
```

**Преимущества:**
- Enterprise-grade надежность
- Высокая производительность и масштабируемость
- Отличная поддержка транзакций
- Соответствие текущим требованиям (задержка до 24 часов)

**Недостатки:**
- Не подходит для real-time сценариев
- Требует JVM ресурсов

### Вариант 2: Real-time Streaming Pipeline (для будущих требований)

```
[EHR Systems] → [HL7v2 Messages] → [Kafka Streams] → [Real-time Transformer] → [FHIR Validator] → [Aidbox Storage]
     ↓              ↓                    ↓                    ↓              ↓              ↓
  Meditech      HL7v2.5.1          Kafka Streams        Spring Boot    FHIR R4       Aidbox
  Epic          Messages            Processing          Microservice  Validation    Database
```

**Преимущества:**
- Минимальная задержка (до 1 часа)
- Подходит для real-time аналитики
- Эффективное использование ресурсов

**Недостатки:**
- Сложность реализации и отладки
- Требует более сложной инфраструктуры

## Выбранная архитектура: Гибридный подход

Для текущих требований используем **Вариант 1** с возможностью эволюции в **Вариант 2**.

### Компоненты пайплайна:

1. **Apache Kafka**
   - Topic: `hl7v2-messages` (3 partitions)
   - Retention: 7 дней
   - Replication factor: 3

2. **Spring Boot Microservice**
   - HL7v2 Parser
   - Data Transformer (HL7v2 → FHIR)
   - FHIR Validator
   - Aidbox Integration

3. **Aidbox Integration**
   - FHIR REST API клиент
   - Обработка ошибок
   - Retry механизмы

## Технологический стек

- **Backend**: Java 17 + Spring Boot 3.x
- **Message Queue**: Apache Kafka 3.x
- **Database**: Aidbox (основная БД)
- **Validation**: FHIR R4 validation libraries
- **Containerization**: Docker + Docker Compose
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)

## Следующие шаги

1. Создание Spring Boot приложения
2. Настройка Kafka producer/consumer
3. Реализация HL7v2 парсера
4. FHIR трансформация и валидация
5. Интеграция с Aidbox
6. Docker контейнеризация
7. Тестирование на реальных HL7v2 сообщениях
