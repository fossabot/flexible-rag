# Changelog

## [1.1.0](https://github.com/thangved/flexible-rag/compare/v1.0.0...v1.1.0) (2024-10-24)


### Features

* add core/rerank ([fab38c4](https://github.com/thangved/flexible-rag/commit/fab38c4ef5ed2e000b05b888af7ec72f829b8d6d))
* implement api/rerank ([706e2eb](https://github.com/thangved/flexible-rag/commit/706e2ebd838a91e1428cd0b5ac44b9230bcec3ec))


### Documentation

* add missing docstring ([4503c5f](https://github.com/thangved/flexible-rag/commit/4503c5f62f1da3f38ba12df17dc1e84183428a96))

## [1.0.0](https://github.com/thangved/flexible-rag/compare/v0.2.0...v1.0.0) (2024-10-23)


### ⚠ BREAKING CHANGES

* remove using langchain in api/vector_store
* remove using langchain in core/vector_store

### Features

* remove using langchain in api/vector_store ([4027718](https://github.com/thangved/flexible-rag/commit/402771891a57b445c963999fe85c1fc411e0a273))
* remove using langchain in chat_llm modules ([a69f749](https://github.com/thangved/flexible-rag/commit/a69f749430888eaf61b02514f1a8a6598c083b4b))
* remove using langchain in core/vector_store ([2fcb655](https://github.com/thangved/flexible-rag/commit/2fcb655534dff579df9c49ae92ad28c39189376f))


### Bug Fixes

* fix black conflict with isort ([1797220](https://github.com/thangved/flexible-rag/commit/17972208c7bbf86aafe81c4d6e6225f8ac5ef353))


### Documentation

* add docstring for CohereChatModel and FakeChatModel ([6c15b73](https://github.com/thangved/flexible-rag/commit/6c15b73e173607801ef643c7eff5481a03a1aa63))
* add docstring for Document and CohereEmbeddingsFunction ([16a3564](https://github.com/thangved/flexible-rag/commit/16a3564a19e3e7895f96547b875e14da73db93e5))

## [0.2.0](https://github.com/thangved/flexible-rag/compare/v0.1.0...v0.2.0) (2024-10-22)


### Features

* add vector store class ([984aee8](https://github.com/thangved/flexible-rag/commit/984aee820a15767f7fa29824224353250fc03b48))
* **api:** implement APIs for vector store ([4f0c0b0](https://github.com/thangved/flexible-rag/commit/4f0c0b0d539833e7e86ba5630f4c19b40b67fc3b))
* implement chat api ([bfeba0e](https://github.com/thangved/flexible-rag/commit/bfeba0ead2e913f1be29cac1f4891d0da81489db))
* implement chat core ([9dd12f9](https://github.com/thangved/flexible-rag/commit/9dd12f9099086d8e2e7d8fc0ef19e19399a97ab8))


### Bug Fixes

* add fallback values for COHERE_API_KEY ([ae835c8](https://github.com/thangved/flexible-rag/commit/ae835c8d77767ac5aa345ae1afd7e95555969e5b))
* resolve lib errors ([5e93fd5](https://github.com/thangved/flexible-rag/commit/5e93fd57f72ffd5f9238ac87908c4a4b282c30cd))
* skip upload cov file ([6fd244b](https://github.com/thangved/flexible-rag/commit/6fd244b29fd43a12aed65de2d290e4aa72b8320f))


### Documentation

* add docstring ([b9ca727](https://github.com/thangved/flexible-rag/commit/b9ca7272c2adbf50dd76df4d8b8c8f3beb10d3a8))
* add docstring for `VectorStore` ([d3841d3](https://github.com/thangved/flexible-rag/commit/d3841d335e6aa266666f981923a579154f712f24))
* add docstring for sample func ([7fee2a0](https://github.com/thangved/flexible-rag/commit/7fee2a05cfd94c417cc6bc6a3f6324dfb2fd9b96))

## 0.1.0 (2024-10-22)

### Features

- init project ([1b9e371](https://github.com/thangved/flexible-rag/commit/1b9e371e01b20f297252ad7846b8989a12b68985))
