import { StepProps } from './types';

export default function Step({ title, complete, error, children }: StepProps) {
  if (error) {
    return (
      <section>
        <h2>{title}</h2>
        ⚠️ Houve um erro
      </section>
    );
  }
  if (complete) {
    return (
      <section>
        <h2>{title}</h2>
        👍 Completo
      </section>
    );
  }
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}
