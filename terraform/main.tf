# =============================================================================
# TERRAFORM INFRASTRUCTURE FOR QUANTUM DL PLATFORM
# BILLIONS OF USERS WORLDWIDE SCALE
# =============================================================================

terraform {
  required_version = ">= 1.6.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.24"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.10"
    }
  }
  
  backend "s3" {
    bucket = "quantum-dl-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
  }
}

# =============================================================================
# PROVIDER CONFIGURATION
# =============================================================================

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "quantum-dl"
      Environment = "production"
      ManagedBy  = "terraform"
      Platform  = "FAANG-scale"
    }
  }
  
  skip_credentials_validation = false
  skip_requesting_account_id  = false
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

# Multi-region provider for disaster recovery
provider "aws" {
  alias   = "eu_west"
  region = "eu-west-1"
  
  default_tags {
    tags = {
      Project     = "quantum-dl"
      Environment = "production"
      Region     = "eu-west"
    }
  }
}

provider "aws" {
  alias   = "ap_southeast"
  region = "ap-southeast-1"
  
  default_tags {
    tags = {
      Project     = "quantum-dl"
      Environment = "production"
      Region     = "ap-southeast"
    }
  }
}

provider "aws" {
  alias   = "ap_northeast"
  region = "ap-northeast-1"
  
  default_tags {
    tags = {
      Project     = "quantum-dl"
      Environment = "production"
      Region     = "ap-northeast"
    }
  }
}

# =============================================================================
# VARIABLES
# =============================================================================

variable "aws_region" {
  description = "Primary AWS region"
  type        = string
  default     = "us-east-1"
}

variable "aws_access_key" {
  description = "AWS access key"
  type        = string
  sensitive   = true
}

variable "aws_secret_key" {
  description = "AWS secret key"
  type        = string
  sensitive   = true
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

variable "primary_domain" {
  description = "Primary domain for the platform"
  type        = string
  default     = "quantum-dl.ai"
}

variable "enable_waf" {
  description = "Enable AWS WAF for DDoS protection"
  type        = bool
  default     = true
}

variable "enable_mfa" {
  description = "Enable MFA for API authentication"
  type        = bool
  default     = true
}

variable "retention_days" {
  description = "Log retention days"
  type        = number
  default     = 90
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

# =============================================================================
# OUTPUTS
# =============================================================================

output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "api_load_balancer_arn" {
  description = "API Load Balancer ARN"
  value       = module.alb.arn
}

output "api_endpoint" {
  description = "API endpoint URL"
  value       = "https://api.${var.primary_domain}"
}

output "cloudfront_distribution_id" {
  description = "CloudFront distribution ID"
  value       = module.cloudfront.cloudfront_id
}

output "redis_cluster_endpoint" {
  description = "Redis cluster endpoint"
  value       = aws_elasticache_cluster.redis.endpoint
}

output "rds_endpoint" {
  description = "RDS endpoint"
  value       = aws_db_instance.postgres.address
}

# =============================================================================
# VPC CONFIGURATION
# =============================================================================

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
  
  name = "quantum-dl-${var.environment}"
  cidr = var.vpc_cidr
  
  # Multi-AZ for high availability
  azs = data.aws_availability_zones.available.names
  
  # Public subnets for load balancers
  public_subnets = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24",
    "10.0.4.0/24",
    "10.0.5.0/24",
    "10.0.6.0/24"
  ]
  
  # Private subnets for application tier
  private_subnets = [
    "10.0.11.0/24",
    "10.0.12.0/24",
    "10.0.13.0/24",
    "10.0.14.0/24",
    "10.0.15.0/24",
    "10.0.16.0/24"
  ]
  
  # Database subnets for RDS
  database_subnets = [
    "10.0.21.0/24",
    "10.0.22.0/24",
    "10.0.23.0/24",
    "10.0.24.0/24",
    "10.0.25.0/24",
    "10.0.26.0/24"
  ]
  
  # ElastiCache subnets
  elasticache_subnets = [
    "10.0.31.0/24",
    "10.0.32.0/24",
    "10.0.33.0/24"
  ]
  
  # Single NAT gateway for cost efficiency
  # Can be upgraded to one per AZ for more redundancy
  enable_nat_gateway     = true
  single_nat_gateway    = false
  one_nat_gateway_per_az = true
  
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  # VPC flow logs for security
  enable_flow_log                      = true
  create_flow_log_cloudwatch_log_group = true
  flow_log_max_aggregation_interval   = 60
  
  # DHCP options for DNS
  enable_dhcp_options                      = true
  dhcp_options_domain_name              = "${var.environment}.quantum-dl.internal"
  dhcp_options_domain_name_servers     = ["AmazonProvidedDNS"]
  
  tags = {
    Environment = var.environment
    Platform    = "FAANG-scale"
  }
}

# =============================================================================
# SECURITY GROUPS
# =============================================================================

resource "aws_security_group" "alb" {
  name        = "quantum-dl-alb-sg"
  description = "Security group for ALB"
  vpc_id      = module.vpc.vpc_id
  
  # Inbound HTTP/HTTPS from anywhere
  ingress {
    description = "HTTPS"
    from_port   = 443
    to_port     = 443
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Outbound to API
  egress {
    description     = "To API"
    from_port       = 8000
    to_port         = 8000
    protocol       = "tcp"
    security_groups = [aws_security_group.api.id]
  }
  
  tags = {
    Environment = var.environment
  }
}

resource "aws_security_group" "api" {
  name        = "quantum-dl-api-sg"
  description = "Security group for API servers"
  vpc_id      = module.vpc.vpc_id
  
  # Inbound from ALB
  ingress {
    description     = "From ALB"
    from_port       = 8000
    to_port         = 8000
    protocol       = "tcp"
    security_groups = [aws_security_group.alb.id]
  }
  
  # Inbound for gRPC
  ingress {
    description     = "gRPC"
    from_port       = 8443
    to_port         = 8443
    protocol       = "tcp"
    security_groups = [aws_security_group.alb.id]
  }
  
  # Inbound from worker CIDR
  ingress {
    description = "From workers"
    from_port    = 8000
    to_port      = 8000
    protocol    = "tcp"
    cidr_blocks = [module.vpc.private_subnets_cidr_blocks[0]]
  }
  
  # Outbound to RDS
  egress {
    description = "To RDS"
    from_port   = 5432
    to_port     = 5432
    protocol   = "tcp"
    cidr_blocks = [module.vpc.database_subnets_cidr_blocks[0]]
  }
  
  # Outbound to ElastiCache
  egress {
    description = "To Redis"
    from_port   = 6379
    to_port     = 6379
    protocol   = "tcp"
    cidr_blocks = [module.vpc.elasticache_subnets_cidr_blocks[0]]
  }
  
  # Outbound to S3
  egress {
    description = "To S3"
    from_port   = 443
    to_port     = 443
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  # Outbound to CloudWatch
  egress {
    description = "To CloudWatch"
    from_port   = 443
    to_port     = 443
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Environment = var.environment
  }
}

resource "aws_security_group" "redis" {
  name        = "quantum-dl-redis-sg"
  description = "Security group for Redis"
  vpc_id      = module.vpc.vpc_id
  
  # Inbound from API
  ingress {
    description     = "From API"
    from_port       = 6379
    to_port         = 6379
    protocol       = "tcp"
    security_groups = [aws_security_group.api.id]
  }
  
  # Inbound from workers
  ingress {
    description     = "From workers"
    from_port       = 6379
    to_port         = 6379
    protocol       = "tcp"
    security_groups = [aws_security_group.worker.id]
  }
  
  tags = {
    Environment = var.environment
  }
}

resource "aws_security_group" "worker" {
  name        = "quantum-dl-worker-sg"
  description = "Security group for workers"
  vpc_id      = module.vpc.vpc_id
  
  # Inbound from API
  ingress {
    description = "From API"
    from_port   = 8888
    to_port     = 8888
    protocol   = "tcp"
    cidr_blocks = [module.vpc.private_subnets_cidr_blocks[0]]
  }
  
  # Outbound to Redis
  egress {
    description = "To Redis"
    from_port  = 6379
    to_port    = 6379
    protocol  = "tcp"
    cidr_blocks = [module.vpc.elasticache_subnets_cidr_blocks[0]]
  }
  
  # Outbound to SQS
  egress {
    description = "To SQS"
    from_port   = 443
    to_port     = 443
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Environment = var.environment
  }
}

# =============================================================================
# RDS POSTGRES
# =============================================================================

resource "aws_db_instance" "postgres" {
  identifier = "quantum-dl-${var.environment}"
  
  engine            = "postgres"
  engine_version   = "15.4"
  instance_class   = "db.r6g.4xlarge"  # 16 vCPU, 128 GiB RAM
  allocated_storage = 4096  # 4TB
  max_allocated_storage = 16384  # 16TB max
  
  # Storage configuration for high performance
  storage_type         = "gp3"
  storage_encrypted    = true
  iops                = 16000
  throughput          = 1000
  
  # Multi-AZ for HA
  multi_az = true
  
  # Connection
  db_name  = "quantumdl"
  username = "quantumadmin"
  password = var.db_password
  
  # VPC
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = module.vpc.database_subnet_group_name
  
  # Performance
  max_connections = 500
  pooler_enabled = true
  
  # Monitoring
  monitoring_interval = 10
  monitoring_role_arn = aws_iam_role.rds_monitoring.arn
  
  # Backup
  backup_retention_period = 30
  backup_window           = "03:00-04:00"
  maintenance_window     = "mon:04:00-mon:05:00"
  
  # Security
  delete_protection = true
  skip_final_snapshot = false
  final_snapshot_identifier = "quantumdl-final-${formatdate("YYYYMMDD", timestamp())}"
  
  # Tags
  tags = {
    Environment = var.environment
    Platform  = "FAANG-scale"
  }
}

# =============================================================================
# ELASTICACHE REDIS CLUSTER
# =============================================================================

resource "aws_elasticache_cluster" "redis" {
  cluster_id           = "quantum-dl-${var.environment}"
  engine              = "redis"
  engine_version     = "7.0"
  node_type          = "cache.r6g.4xlarge"  # 16 vCPU, 127 GiB
  num_cache_nodes   = 6
  port              = 6379
  
  # Cluster mode enabled
  cluster_mode_enabled = true
  num_node_groups    = 3
  replicas_per_node_group = 1
  
  # VPC
  subnet_group_name = module.vpc.elasticache_subnet_group_name
  security_group_ids = [aws_security_group.redis.id]
  
  # Parameters
  parameter_group_name = "default.redis7.cluster.on"
  
  # Logging
  log_delivery_configuration {
    destination      = aws_cloudwatch_log_group.redis_slow.name
    log_format     = "json"
    destination_type = "cloudwatch-logs"
    log_type         = "slow-log"
  }
  
  # Backup
  automatic_failover_enabled = true
  multi_az_enabled        = true
  
  # At-rest encryption
  at_rest_encryption_enabled = true
  transit_encryption_enabled = true
  auth_token_enabled       = true
  
  # Tags
  tags = {
    Environment = var.environment
  }
}

# =============================================================================
# ELASTICACHE MEMCACHED (SESSION STORE)
# =============================================================================

resource "aws_elasticache_cluster" "memcached" {
  cluster_id       = "quantum-dl-session"
  engine         = "memcached"
  engine_version = "1.6.6"
  node_type      = "cache.m6g.xlarge"  # 4 vCPU, 32 GiB
  num_cache_nodes = 10
  port          = 11211
  
  # VPC
  subnet_group_name = module.vpc.elasticache_subnet_group_name
  security_group_ids = [aws_security_group.redis.id]
}

# =============================================================================
# SIMPLE QUEUE SERVICE (SQS)
# =============================================================================

resource "aws_sqs_queue" "inference" {
  name = "quantum-dl-inference-${var.environment}"
  
  # FIFO for ordering
  fifo_queue = false
  
  # Message retention
  message_retention_seconds = 86400  # 24 hours
  
  # Delivery delay
  delay_seconds = 0
  
  # Receive wait time
  receive_wait_time_seconds = 20
  
  # Dead letter queue
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.inference_dlq.arn
    maxReceiveCount   = 5
  })
  
  # Encryption
  sqs_managed_sse_enabled = true
  
  # Tags
  tags = {
    Environment = var.environment
    Platform    = "FAANG-scale"
  }
}

resource "aws_sqs_queue" "inference_dlq" {
  name = "quantum-dl-inference-dlq-${var.environment}"
  
  message_retention_seconds = 1209600  # 14 days
  
  sqs_managed_sse_enabled = true
}

resource "aws_sqs_queue" "training" {
  name = "quantum-dl-training-${var.environment}"
  
  message_retention_seconds = 604800  # 7 days
  receive_wait_time_seconds = 20
  
  # Batch settings for high throughput
  batch_settings {
    max_batch_size         = 10000
    minimum_retry_attempts = 3
    maximum_retry_attempts = 5
  }
  
  sqs_managed_sse_enabled = true
}

resource "aws_sqs_queue" "priority" {
  name = "quantum-dl-priority-${var.environment}"
  
  message_retention_seconds = 3600  # 1 hour for premium users
  receive_wait_time_seconds = 0
  delivery_delay_seconds = 0
  
  sqs_managed_sse_enabled = true
}

# =============================================================================
# APPLICATION LOAD BALANCER
# =============================================================================

module "alb" {
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 8.0"
  
  name = "quantum-dl-${var.environment}"
  
  load_balancer_type = "application"
  load_balancer_cross_zone_enable = true
  
  vpc_id  = module.vpc.vpc_id
  subnets = module.vpc.public_subnets
  
  security_group = aws_security_group.alb.id
  
  # HTTP to HTTPS redirect
  http_listener = true
  http_redirect = true
  
  # HTTPS listener with TLS
  https_listeners = [
    {
      port     = 443
      protocol = "HTTPS"
      certificate_arn = aws_acm_certificate.api.arn
      alpn_policy = "HTTP2"
    }
  ]
  
  # Target groups
  target_groups = [
    {
      name     = "api"
      port     = 8000
      protocol = "HTTP"
      target_type = "instance"
      
      health_check = {
        enabled             = true
        healthy_threshold   = 2
        unhealthy_threshold = 10
        interval          = 10
        matcher           = "200"
        path              = "/health"
        timeout           = 5
      }
      
      # Slow start for new instances
      slow_start = 30
    }
  ]
  
  # Listener rules for routing
  listener_rules = [
    {
      priority = 100
      actions = [{
        type           = "forward"
        target_group_index = 0
      }]
      conditions = [{
        path_pattern = {
          values = ["/api/*"]
        }
      }]
    }
  ]
  
  # Enable WAF
  enable_deletion_protection = false
  
  tags = {
    Environment = var.environment
  }
}

# =============================================================================
# CLOUDFRONT CDN
# =============================================================================

module "cloudfront" {
  source  = "terraform-aws-modules/cloudfront/aws"
  version = "~> 3.0"
  
  name = "quantum-dl-${var.environment}"
  
  enabled = true
  
  # Price class
  price_class = "PriceClass_All"
  
  # Origin
  origin = {
    api = {
      origin_id   = "api-origin"
      domain_name = module.alb.dns_name
      custom_origin_config = {
        http_port              = 80
        https_port             = 443
        origin_protocol_policy = "match-viewer"
        origin_ssl_protocols   = ["TLSv1.2", "TLSv1.3"]
      }
    }
  }
  
  # Default cache policy
  default_cache_behavior = {
    target_origin_id       = "api-origin"
    viewer_protocol_policy = "RedirectToHTTPS"
    compress           = true
    
    allowed_methods        = ["GET", "HEAD", "OPTIONS", "PUT", "PATCH", "POST", "DELETE"]
    cached_methods       = ["GET", "HEAD"]
    
    forwarded_values = {
      query_string = true
      headers    = ["*"]
      
      cookies = {
        forward = "all"
      }
    }
    
    min_ttl     = 0
    default_ttl = 3600
    max_ttl    = 86400
  }
  
  # Custom error responses
  custom_error_responses = [
    {
      error_code           = 403
      error_caching_min_ttl = 60
      response_code       = 403
    },
    {
      error_code           = 404
      error_caching_min_ttl = 60
      response_code       = 404
    },
    {
      error_code           = 500
      error_caching_min_ttl = 0
      response_code       = 500
    }
  ]
  
  # Logging
  logging_config = {
    bucket = "quantum-dl-logs.s3.amazonaws.com"
    prefix = "cloudfront/"
    include_cookies = false
  }
  
  # Tags
  tags = {
    Environment = var.environment
  }
}

# =============================================================================
# WAF WEB APPLICATION FIREWALL
# =============================================================================

resource "aws_wafv2_web_acl" "main" {
  name        = "quantum-dl-waf-${var.environment}"
  description = "WAF for Quantum DL Platform"
  scope      = "CLOUDFRONT"
  
  # Default action
  default_action {
    allow {}
  }
  
  # Rate limiting rule
  rule {
    name     = "RateLimit"
    priority = 1
    
    action {
      block {}
    }
    
    statement {
      rate_based_statement {
        limit              = 10000  # 10k requests per 5 min
        evaluation_window_sec = 300
        aggregate_key_type = "IP"
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name            = "RateLimit"
      sampled_requests_enabled = true
    }
  }
  
  # SQL injection rule
  rule {
    name     = "SQLInjection"
    priority = 2
    
    action {
      block {}
    }
    
    statement {
      byte_match_statement {
        field_to_match {
          query_string {}
        }
        positional_constraint = "CONTAINS"
        search_string    = "'"
        
        text_transformation {
          priority = 1
          type     = "URL_DECODE"
        }
        text_transformation {
          priority = 2
          type     = "HTML_ENTITY_DECODE"
        }
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name            = "SQLInjection"
      sampled_requests_enabled = true
    }
  }
  
  # XSS rule
  rule {
    name     = "XSS"
    priority = 3
    
    action {
      block {}
    }
    
    statement {
      byte_match_statement {
        field_to_match {
          query_string {}
        }
        positional_constraint = "CONTAINS"
        search_string    = "<script>"
        
        text_transformation {
          priority = 1
          type     = "URL_DECODE"
        }
        text_transformation {
          priority = 2
          type     = "LOWERCASE"
        }
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name            = "XSS"
      sampled_requests_enabled = true
    }
  }
  
  # Geo matching - block certain countries
  rule {
    name     = "GeoBlock"
    priority = 4
    
    action {
      block {}
    }
    
    statement {
      geo_match_statement {
        country_codes = ["KP", "IR", "SY"]  # Example - configure as needed
      }
    }
    
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name            = "GeoBlock"
      sampled_requests_enabled = true
    }
  }
  
  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name            = "WAFMain"
    sampled_requests_enabled = true
  }
}

# Associate WAF with CloudFront
resource "aws_wafv2_web_acl_association" "cloudfront" {
  resource_arn = module.cloudfront.arn
  web_acl_arn  = aws_wafv2_web_acl.main.arn
}

# =============================================================================
# IAM ROLES AND POLICIES
# =============================================================================

resource "aws_iam_role" "ecs_task" {
  name = "quantum-dl-ecs-task-${var.environment}"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy" "ecs_task" {
  name = "quantum-dl-ecs-task-policy-${var.environment}"
  role   = aws_iam_role.ecs_task.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "secretsmanager:GetSecretValue",
        "kms:Decrypt",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "dynamodb:*",
        "cloudwatch:PutMetricData",
        "ecr:GetAuthorizationToken",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ]
      Resource = "*"
    }]
  })
}

resource "aws_iam_role" "rds_monitoring" {
  name = "quantum-dl-rds-monitoring-${var.environment}"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "monitoring.rds.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "rds_monitoring" {
  role       = aws_iam_role.rds_monitoring.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonRDSEnhancedMonitoringRole"
}

# =============================================================================
# S3 BUCKETS
# =============================================================================

resource "aws_s3_bucket" "models" {
  bucket = "quantum-dl-models-${var.environment}-${data.aws_caller_identity.current.account_id}"
  
  versioning {
    enabled = true
  }
  
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  
  lifecycle_rule {
    id      = "intelligent-tiering"
    enabled = true
    
    transition {
      days          = 30
      storage_class = "INTELLIGENT_TIERING"
    }
    
    transition {
      days          = 90
      storage_class = "GLACIER"
    }
    
    expiration {
      days = 365
    }
  }
  
  tags = {
    Environment = var.environment
  }
}

resource "aws_s3_bucket" "logs" {
  bucket = "quantum-dl-logs-${var.environment}-${data.aws_caller_identity.current.account_id}"
  
  versioning {
    enabled = true
  }
  
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  
  lifecycle_rule {
    id     = "delete-after-90-days"
    enabled = true
    
    expiration {
      days = 90
    }
  }
}

resource "aws_s3_bucket" "training_data" {
  bucket = "quantum-dl-training-data-${var.environment}-${data.aws_caller_identity.current.account_id}"
  
  versioning {
    enabled = true
  }
  
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

# =============================================================================
# CLOUDWATCH LOG GROUPS
# =============================================================================

resource "aws_cloudwatch_log_group" "api" {
  name              = "/aws/quantum-dl/api/${var.environment}"
  retention_in_days = var.retention_days
  
  lifecycle {
    prevent_delete = false
  }
}

resource "aws_cloudwatch_log_group" "worker" {
  name              = "/aws/quantum-dl/worker/${var.environment}"
  retention_in_days = var.retention_days
}

resource "aws_cloudwatch_log_group" "redis_slow" {
  name              = "/aws/quantum-dl/redis/slow"
  retention_in_days = var.retention_days
}

# =============================================================================
# ROUTE53 DNS
# =============================================================================

resource "aws_route53_zone" "main" {
  name = var.primary_domain
  
  comment = "Quantum DL Platform - ${var.environment}"
  
  tags = {
    Environment = var.environment
  }
}

resource "aws_route53_record" "api" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "api.${var.primary_domain}"
  type    = "A"
  
  alias {
    name                   = module.cloudfront.distribution_domain_name
    zone_id                = module.cloudfront.hosted_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "www.${var.primary_domain}"
  type    = "A"
  
  alias {
    name                   = module.cloudfront.distribution_domain_name
    zone_id                = module.cloudfront.hosted_zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "app" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "app.${var.primary_domain}"
  type    = "A"
  
  alias {
    name                   = module.alb.dns_name
    zone_id                = module.alb.zone_id
    evaluate_target_health = true
  }
}

# =============================================================================
# ACM CERTIFICATE
# =============================================================================

resource "aws_acm_certificate" "api" {
  domain_name       = var.primary_domain
  validation_method = "DNS"
  
  subject_alternative_names = [
    "*.${var.primary_domain}",
    "*.api.${var.primary_domain}",
    "*.app.${var.primary_domain}",
  ]
  
  options {
    certificate_transparency_log_preference = "ENABLED"
  }
  
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_acm_certificate_validation" "api" {
  certificate_arn = aws_acm_certificate.api.arn
  
  validation_record_fqdns = [aws_route53_record.api_validation.fqdn]
}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_caller_identity" "current" {}