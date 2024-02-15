from src.models.payment_model import Payment, PaymentStatus
from src.schemas.paymentSchema import PaymentCreate
from src.services.paymentService import PaymentManagementActuator


def test_add_payment(mock_db):
    data = PaymentCreate(name="Completed", order_id=1, amount=100.0, provider="PayPal")
    actuator = PaymentManagementActuator()

    # Mocking the add operation
    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    assert actuator.add_payment(data, mock_db) is True


def test_get_payment_by_id(mock_db):
    payment_id = 1
    mock_payment = Payment(
        id=1,
        order_id=1,
        amount=100.0,
        provider="PayPal",
        status=PaymentStatus.COMPLETED,
    )
    mock_db.query.return_value.get.return_value = mock_payment

    actuator = PaymentManagementActuator()
    payment = actuator.get_payment_by_id(payment_id, mock_db)
    assert payment.id == 1


def test_update_payment_status(mock_db):
    payment_id = 1
    data = PaymentCreate(name="Completed", order_id=1, amount=200.0, provider="PayPal")
    mock_payment = Payment(
        id=1,
        order_id=1,
        amount=100.0,
        provider="PayPal",
        status=PaymentStatus.COMPLETED,
    )
    mock_db.query.return_value.get.return_value = mock_payment

    # Mocking the commit operation
    mock_db.commit.return_value = None

    actuator = PaymentManagementActuator()
    assert actuator.update_payment_status(payment_id, data, mock_db) is True


def test_delete_payment(mock_db):
    payment_id = 1
    mock_payment = Payment(
        id=1,
        order_id=1,
        amount=100.0,
        provider="PayPal",
        status=PaymentStatus.COMPLETED,
    )
    mock_db.query.return_value.get.return_value = mock_payment

    # Mocking the commit operation
    mock_db.commit.return_value = None

    actuator = PaymentManagementActuator()
    assert actuator.delete_payment(payment_id, mock_db) is True
