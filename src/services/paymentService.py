from sqlalchemy.orm import Session
from src.models.payment_model import Payment,PaymentStatus
from src.schemas.paymentSchema import PaymentCreate,PaymentShow
from datetime import datetime

class PaymentManagementActuator:
    def _getPaymentStatus(self, name):
        if "PENDING" in name.upper():
            return PaymentStatus.PENDING
        elif "COMPLETED" in name.upper():
            return PaymentStatus.COMPLETED
        elif "FAILED" in name.upper():
            return PaymentStatus.FAILED

    def add_payment(self,data:PaymentCreate, db:Session):
        status = self._getPaymentStatus(data.name)
        new_payment = Payment(
            order_id=data.order_id,
            amount=data.amount,
            provider=data.provider,
            status=status,
            created_at=datetime.utcnow(),
            modified_at=datetime.utcnow()
        )
        try:
            db.add(new_payment)
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def get_payment_by_id(self, payment_id:int,db:Session):
        payment = db.query(Payment).get(payment_id)
        if payment:
            return PaymentShow(**payment.__dict__)
        return None

    def update_payment_status(self, payment_id,data:PaymentCreate,db:Session):
        payment = db.query(Payment).get(payment_id)
        if payment:
            if data.id:
                payment.id=data.id
            if data.order_id:
                payment.order_id=data.order_id
            if data.amount:
                payment.amount = data.amount
            if data.provider:
                payment.provider=data.provider
            try:
                db.commit()
                return True
            except Exception as e:
                print(e)
                db.rollback()
                return False
        return False
    def delete_payment(self, payment_id,db: Session):
        payment = db.query(Payment).get(payment_id)
        if payment:
            db.delete(payment)
            db.commit()
            return True
        return False
