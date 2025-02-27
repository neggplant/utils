#!/bin/bash

# 参数设置
NAME="xxxx"  # Deployment 和 HPA 名称
NAMESPACE="xxxx"  # 命名空间
IMAGE=""  # 容器镜像，没有协议
FLASK_CONFIG="cn"  # Flask 配置
TZ="Asia/Shanghai"  # 时区
SERVICE_NAME="xxxx-svc"  # 服务名称
APP_LABEL="xxxx"  # 应用标签
INGRESS_NAME="xxxx-ingress"  # Ingress 名称
HOST="xxxx.com"  # 域名
# 以下可选
REPLICAS=2  # Deployment 副本数
MIN_REPLICAS=2  # HPA 最小副本数
MAX_REPLICAS=200  # HPA 最大副本数
TARGET_UTILIZATION=90  # HPA CPU 利用率目标
SERVICE_PORT=6666  # 服务端口
TARGET_PORT=6666  # 目标端口

# 创建 Deployment YAML
sed "s|{{NAME}}|$NAME|g; s|{{NAMESPACE}}|$NAMESPACE|g; s|{{REPLICAS}}|$REPLICAS|g; s|{{IMAGE}}|$IMAGE|g; s|{{FLASK_CONFIG}}|$FLASK_CONFIG|g; s|{{TZ}}|$TZ|g" deployment.yaml > deployment-temp.yaml

# 应用 Deployment
kubectl apply -f deployment-temp.yaml -n $NAMESPACE

# 创建 HPA YAML
sed "s|{{NAME}}|$NAME|g; s|{{NAMESPACE}}|$NAMESPACE|g; s|{{MIN_REPLICAS}}|$MIN_REPLICAS|g; s|{{MAX_REPLICAS}}|$MAX_REPLICAS|g; s|{{DEPLOYMENT_NAME}}|$NAME|g; s|{{TARGET_UTILIZATION}}|$TARGET_UTILIZATION|g" hpa.yaml > hpa-temp.yaml

# 应用 HPA
kubectl apply -f hpa-temp.yaml -n $NAMESPACE

# 创建 Service YAML
sed "s|{{SERVICE_NAME}}|$SERVICE_NAME|g; s|{{NAMESPACE}}|$NAMESPACE|g; s|{{APP_LABEL}}|$APP_LABEL|g; s|{{SERVICE_PORT}}|$SERVICE_PORT|g; s|{{TARGET_PORT}}|$TARGET_PORT|g" service.yaml > service-temp.yaml

# 应用 Service
kubectl apply -f service-temp.yaml -n $NAMESPACE

# 创建 Ingress YAML
sed "s|{{INGRESS_NAME}}|$INGRESS_NAME|g; s|{{NAMESPACE}}|$NAMESPACE|g; s|{{HOST}}|$HOST|g; s|{{SERVICE_NAME}}|$SERVICE_NAME|g; s|{{SERVICE_PORT}}|$SERVICE_PORT|g" ingress.yaml > ingress-temp.yaml

# 应用 Ingress
kubectl apply -f ingress-temp.yaml -n $NAMESPACE

# 输出状态
kubectl get deployments -n $NAMESPACE
kubectl get hpa -n $NAMESPACE
kubectl get svc -n $NAMESPACE
kubectl get ingress -n $NAMESPACE

# 清理临时文件
rm deployment-temp.yaml hpa-temp.yaml service-temp.yaml ingress-temp.yaml